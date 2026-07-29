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
        self.assertEqual(
            resolve_chart_name(self.registry, "瀑布图"),
            ["contribution-waterfall-chart", "tumor-response-waterfall-plot"],
        )

    def test_new_source_taxonomy_routes(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "词云"), ["word-cloud"])
        self.assertEqual(resolve_chart_name(self.registry, "鱼骨图"), ["ishikawa-diagram"])
        self.assertEqual(resolve_chart_name(self.registry, "DAG"), ["causal-dag"])

    def test_materials_and_electrochemistry_routes(self) -> None:
        expected = {
            "XPS peak fitting": ["xps-peak-deconvolution-plot"],
            "WT-EXAFS": ["exafs-wavelet-transform-map"],
            "CV curve": ["cyclic-voltammetry-curve"],
            "GCD profile": ["galvanostatic-charge-discharge-curve"],
            "rate capability test": ["battery-rate-capability-plot"],
            "long-term cycling plot": ["battery-cycling-stability-plot"],
            "b-value plot": ["peak-current-scan-rate-log-log-plot"],
            "capacitive contribution plot": ["capacitive-diffusion-contribution-plot"],
        }
        for query, chart_ids in expected.items():
            with self.subTest(query=query):
                self.assertEqual(resolve_chart_name(self.registry, query), chart_ids)

    def test_chord_diagram_route(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "Chord Diagram"), ["chord-diagram"])

    def test_unknown_name_is_not_guessed(self) -> None:
        self.assertEqual(resolve_chart_name(self.registry, "不存在的万能神图"), [])


if __name__ == "__main__":
    unittest.main()
