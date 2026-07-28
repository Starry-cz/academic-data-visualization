from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from chart_registry_lib import load_registry
from generate_chart_catalog import expected_outputs


class CatalogGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.outputs = expected_outputs(load_registry())

    def test_generated_files_match_registry(self) -> None:
        stale = [
            str(path.relative_to(ROOT))
            for path, expected in self.outputs.items()
            if not path.exists() or path.read_text(encoding="utf-8") != expected
        ]
        self.assertEqual(stale, [])

    def test_exactly_24_category_documents(self) -> None:
        category_docs = [
            path for path in self.outputs
            if path.parent == ROOT / "references" / "chart-types"
        ]
        self.assertEqual(len(category_docs), 24)
        self.assertEqual(
            len(list((ROOT / "references" / "chart-types").glob("*.md"))),
            24,
        )

    def test_readme_blocks_are_generated(self) -> None:
        for name in ("README.md", "README_EN.md"):
            text = self.outputs[ROOT / name]
            self.assertIn("chart-registry:summary:start", text)
            self.assertIn("665", text)
            self.assertIn("714", text)
            self.assertIn("34", text)


if __name__ == "__main__":
    unittest.main()
