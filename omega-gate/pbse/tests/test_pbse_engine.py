import tempfile
import unittest
from pathlib import Path

from pbse.pbse_engine import PBSEngine


class PBSEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.rules = Path(self.tmp_dir.name) / "rules.yaml"
        self.audit = Path(self.tmp_dir.name) / "decisions.log"
        self.rules.write_text(
            '{"escalate_when_missing": ["hypothesis.traceable", "hypothesis.evidence_hash"]}',
            encoding="utf-8",
        )
        self.engine = PBSEngine(rules_path=self.rules, audit_path=self.audit)

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_pass_for_complete_submission(self) -> None:
        verdict = self.engine.judge(
            {"id": "H1", "formal": True, "traceable": True, "evidence_hash": "abc"},
            {"id": "P1", "auditable": True, "complete": True},
        )
        self.assertEqual(verdict.decision, "PASS")

    def test_block_for_nonformal_hypothesis(self) -> None:
        verdict = self.engine.judge(
            {"id": "H1", "formal": False, "traceable": True, "evidence_hash": "abc"},
            {"id": "P1", "auditable": True, "complete": True},
        )
        self.assertEqual(verdict.decision, "BLOCK")

    def test_escalate_for_missing_traceability(self) -> None:
        verdict = self.engine.judge(
            {"id": "H1", "formal": True, "traceable": False, "evidence_hash": "abc"},
            {"id": "P1", "auditable": True, "complete": True},
        )
        self.assertEqual(verdict.decision, "ESCALATE")


if __name__ == "__main__":
    unittest.main()
