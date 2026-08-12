from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_palette_library import audit_palette_library


class PaletteLibraryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads((ROOT / "references" / "palette-library.json").read_text(encoding="utf-8"))
        self.theme_ids = [theme["id"] for theme in self.payload["themes"]]

    def test_palette_audit_rejects_near_duplicates(self) -> None:
        """主题内近似分类色与可合并主题必须在提交前清零。"""
        colour_findings, theme_findings = audit_palette_library()
        self.assertEqual(colour_findings, [])
        self.assertEqual(theme_findings, [])

    def test_readmes_show_every_registered_theme_once(self) -> None:
        for name in ("README.md", "README_EN.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            block = text.split("<!-- palette-gallery:start -->", 1)[1].split("<!-- palette-gallery:end -->", 1)[0]
            ids = re.findall(r"assets/palette-gallery/([a-z0-9-]+)\.png", block)
            self.assertEqual(ids, self.theme_ids, name)

    def test_palette_preview_assets_match_the_registry(self) -> None:
        gallery = ROOT / "assets" / "palette-gallery"
        for suffix in (".png", ".svg", ".pdf"):
            self.assertEqual({path.stem for path in gallery.glob(f"*{suffix}")}, set(self.theme_ids), suffix)

    def test_merged_theme_is_not_left_in_docs_or_registry(self) -> None:
        self.assertNotIn("quiet-atlas", self.theme_ids)
        for path in (ROOT / "references" / "color-palettes.md", ROOT / "references" / "journal-intel.md"):
            self.assertNotIn("quiet-atlas", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
