from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from chart_registry_lib import load_registry
from query_chart import chart_summary, question_score


class QueryChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = load_registry()
        cls.by_id = {chart["id"]: chart for chart in cls.registry["charts"]}

    def test_compact_summary_exposes_truthful_routing_fields(self) -> None:
        summary = chart_summary(self.by_id["forest-plot"])
        self.assertEqual(summary["implementation_status"], "production_verified")
        self.assertEqual(summary["verification_status"], "release_passed")
        self.assertTrue(summary["asset_path"].startswith("templates/production-verified/"))

    def test_question_search_prefers_relevant_chart(self) -> None:
        forest = question_score(self.by_id["forest-plot"], "比较多个效应量及其置信区间")
        sankey = question_score(self.by_id["sankey-diagram"], "比较多个效应量及其置信区间")
        self.assertGreater(forest, sankey)


if __name__ == "__main__":
    unittest.main()
