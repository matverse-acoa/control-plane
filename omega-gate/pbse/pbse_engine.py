"""PBSE engine for deterministic admissibility decisions."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Verdict:
    decision: str
    reason: str
    proof_hash: str
    timestamp: str


class PBSEngine:
    """Deterministic constitutional firewall for hypotheses/protocols."""

    def __init__(self, rules_path: Path | None = None, audit_path: Path | None = None) -> None:
        base_dir = Path(__file__).resolve().parent
        self.rules_path = rules_path or base_dir / "decision_rules.yaml"
        self.audit_path = audit_path or base_dir / "audit_log" / "decisions.log"
        self.rules = self._load_rules()

    def _load_rules(self) -> dict[str, Any]:
        """Load rules file in JSON-compatible YAML format."""
        with self.rules_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def judge(self, hypothesis: dict[str, Any], protocol: dict[str, Any]) -> Verdict:
        missing = []
        if not hypothesis.get("formal"):
            missing.append("hypothesis.formal")
        if not hypothesis.get("traceable"):
            missing.append("hypothesis.traceable")
        if not hypothesis.get("evidence_hash"):
            missing.append("hypothesis.evidence_hash")
        if not protocol.get("auditable"):
            missing.append("protocol.auditable")
        if not protocol.get("complete"):
            missing.append("protocol.complete")

        escalation_fields = set(self.rules.get("escalate_when_missing", []))
        should_escalate = any(field in escalation_fields for field in missing)

        if not missing:
            decision = "PASS"
            reason = "All admissibility conditions satisfied"
        elif should_escalate:
            decision = "ESCALATE"
            reason = f"Manual constitutional review required ({', '.join(missing)})"
        else:
            decision = "BLOCK"
            reason = f"Admissibility failure ({', '.join(missing)})"

        proof_hash = self._proof_hash(hypothesis, protocol, decision, reason)
        verdict = Verdict(
            decision=decision,
            reason=reason,
            proof_hash=proof_hash,
            timestamp=datetime.now(UTC).isoformat(),
        )
        self._append_audit(verdict, hypothesis, protocol)
        return verdict

    def _proof_hash(
        self,
        hypothesis: dict[str, Any],
        protocol: dict[str, Any],
        decision: str,
        reason: str,
    ) -> str:
        payload = {
            "hypothesis": hypothesis,
            "protocol": protocol,
            "decision": decision,
            "reason": reason,
        }
        normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha3_256(normalized.encode("utf-8")).hexdigest()

    def _append_audit(
        self,
        verdict: Verdict,
        hypothesis: dict[str, Any],
        protocol: dict[str, Any],
    ) -> None:
        self.audit_path.parent.mkdir(parents=True, exist_ok=True)
        entry = {
            "timestamp": verdict.timestamp,
            "decision": verdict.decision,
            "reason": verdict.reason,
            "proof_hash": verdict.proof_hash,
            "hypothesis_id": hypothesis.get("id"),
            "protocol_id": protocol.get("id"),
        }
        with self.audit_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
