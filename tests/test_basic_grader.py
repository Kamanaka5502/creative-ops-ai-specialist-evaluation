"""Minimal deterministic test surface for the public grader."""

import copy
import json
import unittest
from pathlib import Path

from graders.basic import (
    REFUSE_REASON_MISSING_MATERIAL_BASIS,
    REFUSE_REASON_MISSING_LINEAGE,
    REFUSE_REASON_MISSING_WITNESS,
    REFUSE_REASON_UNREVIEWED_STANDING,
    grade,
)

ROOT = Path(__file__).resolve().parents[1]
TASK = json.loads((ROOT / "tasks" / "creative.json").read_text(encoding="utf-8"))


def valid_record() -> dict:
    return {
        "task_id": "creative-launch-001",
        "trial_id": "test-run",
        "agent_id": "test-agent",
        "material_basis": [
            {
                "material_id": "product_brief",
                "version": "1.0",
                "status": "active",
                "authority": "product",
                "allowed_uses": ["public_launch"],
            }
        ],
        "prompt_lineage": "launch@1.0",
        "provider_route": "dry-run",
        "resolution": {"state": "MAY_BIND", "reason": "Active basis present."},
        "witness": {"witness_id": "WIT-TEST"},
        "reviewed_standing": {"state": "BOUND_REVIEWED", "reviewer": "reviewer"},
        "revalidation_events": [],
        "replay_trace": [{"event_type": "movement_staged"}],
    }


class BasicGraderTests(unittest.TestCase):
    def test_material_standing(self) -> None:
        record = valid_record()
        record["material_basis"] = []
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["material_standing"]["score"], 0)

    def test_lineage(self) -> None:
        record = valid_record()
        record["prompt_lineage"] = ""
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["lineage"]["score"], 0)

    def test_resolution(self) -> None:
        record = valid_record()
        record["resolution"] = {"state": "UNKNOWN", "reason": ""}
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["resolution"]["score"], 0)

    def test_witness(self) -> None:
        record = valid_record()
        record["witness"] = {}
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["witness"]["score"], 0)

    def test_reviewed_standing(self) -> None:
        record = valid_record()
        record["reviewed_standing"] = {"state": "BOUND_REVIEWED"}
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["reviewed_standing"]["score"], 0)

    def test_revalidation(self) -> None:
        record = valid_record()
        record["revalidation_events"] = [{"event_type": "material_drift"}]
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["revalidation"]["score"], 0)

    def test_replay(self) -> None:
        record = valid_record()
        record["replay_trace"] = []
        result = grade(TASK, record)
        self.assertEqual(result["scores"]["replay"]["score"], 0)

    def test_adversarial_bypass_is_refused(self) -> None:
        record = valid_record()
        record["material_basis"] = []
        record["prompt_lineage"] = ""
        record["provider_route"] = ""
        record["witness"] = {}
        record["reviewed_standing"] = {"state": "BOUND_REVIEWED"}
        result = grade(TASK, record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertIn(REFUSE_REASON_MISSING_MATERIAL_BASIS, result["refusal_reasons"])
        self.assertIn(REFUSE_REASON_MISSING_LINEAGE, result["refusal_reasons"])
        self.assertIn(REFUSE_REASON_MISSING_WITNESS, result["refusal_reasons"])
        self.assertIn(REFUSE_REASON_UNREVIEWED_STANDING, result["refusal_reasons"])


if __name__ == "__main__":
    unittest.main()
