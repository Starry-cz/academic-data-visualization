from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from manifest_lib import find_asset_manifests, load_manifest, sha256_file, validate_manifest
from qa_validator import audit_source


class ManifestV2Tests(unittest.TestCase):
    def test_text_hash_is_stable_across_line_endings(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root)
            lf_path = root / "lf.json"
            crlf_path = root / "crlf.json"
            lf_path.write_bytes(b'{\n  "status": "passed"\n}\n')
            crlf_path.write_bytes(b'{\r\n  "status": "passed"\r\n}\r\n')
            self.assertEqual(sha256_file(lf_path), sha256_file(crlf_path))

    def test_manifest_order_is_platform_independent(self) -> None:
        paths = find_asset_manifests()
        expected = sorted(paths, key=lambda path: path.relative_to(ROOT).as_posix().casefold())
        self.assertEqual(paths, expected)

    def test_all_asset_manifests_validate(self) -> None:
        errors: list[str] = []
        for path in find_asset_manifests():
            errors.extend(f"{path.relative_to(ROOT)}: {item}" for item in validate_manifest(load_manifest(path), path.parent))
        self.assertEqual(errors, [])

    def test_verified_assets_have_real_release_evidence(self) -> None:
        manifests = [load_manifest(path) for path in find_asset_manifests()]
        verified = [manifest for manifest in manifests if manifest["asset_status"] == "production_verified"]
        self.assertEqual(len(verified), 12)
        for manifest in verified:
            asset_dir = ROOT / "templates" / "production-verified" / manifest["asset_id"]
            evidence = json.loads((asset_dir / manifest["verification"]["evidence"]).read_text(encoding="utf-8"))
            self.assertNotIn(str(ROOT), json.dumps(evidence))
            self.assertEqual(evidence["visual_review"]["status"], "passed")
            self.assertTrue(evidence["modes"]["demo"]["qa_passed"])
            self.assertTrue(evidence["modes"]["input"]["qa_passed"])

    def test_production_entrypoint_passes_strict_source_audit(self) -> None:
        findings = audit_source(ROOT / "scripts" / "verified_template.py", production_interface=True)
        failures = [finding for finding in findings if not finding.pass_ and finding.severity == "FAIL"]
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
