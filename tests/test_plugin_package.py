from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PluginPackageTests(unittest.TestCase):
    def test_plugin_points_to_standard_skills_directory(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "academic-data-visualization")
        self.assertEqual(manifest["version"], "2.0.0")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertTrue((ROOT / "skills" / "academic-data-visualization" / "SKILL.md").is_file())

    def test_packaged_palette_registry_matches_source(self) -> None:
        source = ROOT / "references" / "palette-library.json"
        packaged = ROOT / "skills" / "academic-data-visualization" / "references" / "palette-library.json"
        self.assertEqual(packaged.read_bytes(), source.read_bytes())

    def test_package_contains_no_runtime_cache(self) -> None:
        package = ROOT / "skills" / "academic-data-visualization"
        caches = [path for path in package.rglob("*") if path.name in {"__pycache__", ".mplconfig"}]
        self.assertEqual(caches, [])


if __name__ == "__main__":
    unittest.main()
