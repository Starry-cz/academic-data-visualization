from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from chart_registry_lib import load_registry, source_memberships, status_counts
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

    def test_source_memberships_are_complete_for_available_source(self) -> None:
        pairs = source_memberships()
        self.assertEqual(
            len(pairs),
            self.registry["source_expectation"]["available_source_memberships"],
        )
        self.assertEqual(len(pairs), len(set(pairs)))

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
