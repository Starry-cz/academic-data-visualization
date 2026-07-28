from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from chart_registry_lib import load_registry, parse_source_taxonomy, source_memberships, status_counts
from check_chart_registry import validate_registry


class ChartRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = load_registry()

    def test_registry_is_valid(self) -> None:
        self.assertEqual(validate_registry(), [])

    def test_all_24_categories_exist(self) -> None:
        self.assertEqual(
            [category["id"] for category in self.registry["categories"]],
            [f"{index:02d}" for index in range(1, 25)],
        )
        self.assertEqual(
            self.registry["categories"][14]["name_zh"],
            "质性研究与文本分析图",
        )
        self.assertEqual(
            self.registry["categories"][22]["name_zh"],
            "研究流程与论文规范图",
        )

    def test_all_714_source_memberships_are_mapped(self) -> None:
        pairs = source_memberships()
        entries = parse_source_taxonomy()
        expectation = self.registry["source_expectation"]
        self.assertEqual(len(entries), 714)
        self.assertEqual(len(pairs), 714)
        self.assertEqual(expectation["declared_memberships"], 714)
        self.assertEqual(expectation["available_source_memberships"], 714)
        self.assertTrue(expectation["source_complete"])
        self.assertFalse(any(entry["canonical_id"] is None for entry in entries))

    def test_registry_origin_matches_source_memberships(self) -> None:
        for chart in self.registry["charts"]:
            if chart["registry_origin"] == "source_taxonomy":
                self.assertGreater(len(chart["source_memberships"]), 0)
            else:
                self.assertEqual(chart["registry_origin"], "repository_extension")
                self.assertEqual(chart["source_memberships"], [])

    def test_status_counts_and_production_truth(self) -> None:
        counts = status_counts(self.registry)
        self.assertEqual(counts["production_template"], 34)
        self.assertGreater(counts["reusable_pattern"], 0)
        self.assertGreater(counts["on_demand"], 0)
        for chart in self.registry["charts"]:
            if chart["implementation_status"] == "production_template":
                self.assertIsNotNone(chart["asset_path"])
            else:
                self.assertIsNone(chart["asset_path"])


if __name__ == "__main__":
    unittest.main()
