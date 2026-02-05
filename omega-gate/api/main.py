"""Minimal API facade for Omega Gate submissions."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pbse.pbse_engine import PBSEngine


def submit(payload: dict[str, Any], engine: PBSEngine | None = None) -> dict[str, Any]:
    """Process a payload compatible with /api/submit semantics."""
    pbse = engine or PBSEngine()
    hypothesis = payload.get("hypothesis", {})
    protocol = payload.get("protocol", {})
    verdict = pbse.judge(hypothesis, protocol)
    return asdict(verdict)


if __name__ == "__main__":
    sample = {
        "hypothesis": {"id": "HYP-001", "formal": True, "traceable": True, "evidence_hash": "abc"},
        "protocol": {"id": "PROTO-001", "auditable": True, "complete": True},
    }
    print(json.dumps(submit(sample), ensure_ascii=False, indent=2))
