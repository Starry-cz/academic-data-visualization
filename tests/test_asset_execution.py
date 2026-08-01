from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from manifest_lib import manifest_by_chart_id
from palette_lib import THEMES
from run_asset import run_asset


class AssetExecutionTests(unittest.TestCase):
    def test_forest_template_runs_and_passes_output_qa(self) -> None:
        manifest_path, _ = manifest_by_chart_id("forest-plot")
        with tempfile.TemporaryDirectory(prefix="adv-test-") as temp:
            output = Path(temp) / "output"
            record = run_asset(
                manifest_path=manifest_path,
                output_dir=output,
                input_path=None,
                demo=True,
                profile="report_web",
                theme="auto",
                seed=20260801,
                config=None,
                timeout=120,
                overwrite=False,
            )
            self.assertTrue(record["qa_passed"])
            self.assertEqual(record["command"][0:2], ["python", "scripts/verified_template.py"])
            self.assertNotIn(str(ROOT), json.dumps(record))
            report = json.loads((output / "qa-report.json").read_text(encoding="utf-8"))
            self.assertTrue(report["passed"])
            self.assertEqual(record["theme"], "literature-clinical")
            metadata = json.loads((output / "figure-metadata.json").read_text(encoding="utf-8"))
            expected = THEMES["literature-clinical"]
            self.assertEqual(metadata["palette"]["categorical"], expected["categorical"])
            self.assertEqual(metadata["palette"]["diverging"], expected["diverging"])
            self.assertTrue((output / "figure.svg").is_file())
            self.assertTrue((output / "figure.pdf").is_file())


if __name__ == "__main__":
    unittest.main()
