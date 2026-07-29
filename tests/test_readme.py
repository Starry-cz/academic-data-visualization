from __future__ import annotations

import re
import struct
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README_NAMES = ("README.md", "README_EN.md")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_TARGET = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
CARD_DIR = ROOT / "assets" / "figure-atlas" / "readme-cards"
SQUARE_CARDS = {
    "3Dheatmap.png",
    "density_heatmap.png",
    "PCA.png",
    "auroc.png",
    "CorrelationDensity.png",
    "Correlationmatrix.png",
    "GroupCorrelationmatrix.png",
    "radar.png",
    "RidgePlot.png",
    "bubble_scatter.png",
    "correlation_bubble_matrix.png",
    "correlation_network.png",
}
WIDE_CARDS = {
    "bar.png",
    "GroupedBarChart.png",
    "MantelCorrelation.png",
    "violin_chart.png",
    "trend.png",
    "StackedBarScatter.png",
    "Frequency_3DHeatmap.png",
    "sankey.png",
    "stacked_area.png",
    "geographic_bubble_map.png",
}


def local_targets(text: str) -> set[str]:
    """提取 README 中需要在仓库内真实存在的链接与图片路径。"""
    targets = {
        target.strip().strip("<>")
        for pattern in (MARKDOWN_LINK, HTML_TARGET)
        for target in pattern.findall(text)
    }
    return {
        unquote(target.split("#", 1)[0].split("?", 1)[0])
        for target in targets
        if target
        and not target.startswith(("#", "http://", "https://", "mailto:"))
    }


def png_dimensions(path: Path) -> tuple[int, int]:
    """直接读取 PNG IHDR，避免 README 回归测试依赖图像处理库。"""
    header = path.read_bytes()[:24]
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Not a PNG: {path}")
    return struct.unpack(">II", header[16:24])


class ReadmeTests(unittest.TestCase):
    def test_local_links_exist(self) -> None:
        missing: list[str] = []
        for name in README_NAMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            for target in sorted(local_targets(text)):
                if not (ROOT / target).exists():
                    missing.append(f"{name}: {target}")
        self.assertEqual(missing, [])

    def test_public_metrics_match_current_baseline(self) -> None:
        for name in README_NAMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("714 / 714", text)
            self.assertIn("34 / 34", text)
            self.assertIn("88 / 88", text)
            self.assertNotIn("Figure_patterns-96", text)
            self.assertNotIn("**40 / 40**", text)

    def test_visual_banner_replaces_duplicate_title(self) -> None:
        for name in README_NAMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotIn(
                '<h1 align="center">Academic Data Visualization</h1>',
                text,
            )
            self.assertLess(
                text.index("academic-data-visualization-workflow-v5.png"),
                text.index("From research question")
                if name == "README_EN.md"
                else text.index("从研究问题到投稿级图表"),
            )

    def test_language_switch_defaults_to_chinese(self) -> None:
        chinese = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn(
            '<strong>简体中文</strong> · <a href="README_EN.md">English</a>',
            chinese,
        )
        self.assertIn(
            '<a href="README.md">简体中文</a> · <strong>English</strong>',
            english,
        )
        self.assertIn("从研究问题到投稿级图表", chinese)
        self.assertIn("From research question to publication-ready figure", english)

    def test_all_table_cells_declare_widths(self) -> None:
        for name in README_NAMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            cells_without_width = re.findall(r"<t[dh]\b(?![^>]*\bwidth=)[^>]*>", text)
            self.assertEqual(cells_without_width, [], name)

    def test_every_table_is_forced_to_readme_width(self) -> None:
        for name in README_NAMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            tables = re.findall(r"<table\b.*?</table>", text, flags=re.DOTALL)
            self.assertGreater(len(tables), 0, name)
            for index, table in enumerate(tables, start=1):
                self.assertEqual(
                    table.count("assets/readme/table-full-width-spacer.svg"),
                    1,
                    f"{name} table {index}",
                )

    def test_gallery_uses_22_equal_canvas_cards(self) -> None:
        self.assertEqual(
            {path.name for path in CARD_DIR.glob("*.png")},
            SQUARE_CARDS | WIDE_CARDS,
        )
        for name in SQUARE_CARDS:
            self.assertEqual(png_dimensions(CARD_DIR / name), (1800, 1800))
        for name in WIDE_CARDS:
            self.assertEqual(png_dimensions(CARD_DIR / name), (1800, 1000))
        for readme_name in README_NAMES:
            text = (ROOT / readme_name).read_text(encoding="utf-8")
            gallery_refs = set(
                re.findall(r"assets/figure-atlas/readme-cards/([^\"?]+\.png)", text)
            )
            self.assertEqual(gallery_refs, SQUARE_CARDS | WIDE_CARDS)


if __name__ == "__main__":
    unittest.main()
