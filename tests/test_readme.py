from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README_NAMES = ("README.md", "README_EN.md")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_TARGET = re.compile(r"""(?:href|src)=["']([^"']+)["']""")


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

    def test_title_precedes_visual_banner(self) -> None:
        for name in README_NAMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertLess(
                text.index("<h1"),
                text.index("academic-data-visualization-workflow-v5.png"),
            )


if __name__ == "__main__":
    unittest.main()
