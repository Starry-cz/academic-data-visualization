from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from chart_registry_lib import load_registry, resolve_chart_name


class ChartRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = load_registry()

    def test_chinese_name(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "相关网络图"), ["correlation-network"])

    def test_english_alias_and_abbreviation(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "AUROC"), ["roc-curve"])
        self.assertEqual(resolve_chart_name(self.registry, "PR curve"), ["precision-recall-curve"])

    def test_spacing_and_dash_normalization(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "Q Q plot"), ["qq-plot"])

    def test_declared_ambiguity(self) -> None:
        self.assertEqual(
            resolve_chart_name(self.registry, "漏斗图"),
            ["meta-analysis-funnel-plot", "conversion-funnel-chart"],
        )
        self.assertEqual(
            resolve_chart_name(self.registry, "棒棒糖图"),
            ["lollipop-chart", "mutation-lollipop-plot"],
        )

    def test_unknown_name_is_not_guessed(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "不存在的万能神图"), [])


if __name__ == "__main__":
    unittest.main()
