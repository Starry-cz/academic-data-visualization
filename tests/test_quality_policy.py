from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from qa_validator import check_cl3_dpi


class QualityPolicyTests(unittest.TestCase):
    def test_skill_routes_delivery_profile_before_styling(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/delivery-profiles.md", skill)
        self.assertIn("keynote_screen", skill)
        self.assertNotIn("Do not use for interactive dashboards, presentation slides", skill)

    def test_multi_panel_hierarchy_is_conditional(self) -> None:
        layout = (ROOT / "references" / "multipanel-layout.md").read_text(encoding="utf-8")
        brief = (ROOT / "references" / "figure-design-brief.md").read_text(encoding="utf-8")
        self.assertIn("Conditional Hero Panel Principle", layout)
        self.assertIn("equal grid", layout)
        self.assertNotIn("Every multi-panel figure needs one", layout)
        self.assertIn("Hierarchy: [equal grid", brief)

    def test_schematic_order_depends_on_decoding_need(self) -> None:
        layout = (ROOT / "references" / "multipanel-layout.md").read_text(encoding="utf-8")
        self.assertIn("Decode before interpret", layout)
        self.assertNotIn("Data before schematics", layout)

    def test_300_dpi_is_valid_fallback_for_print_raster(self) -> None:
        self.assertTrue(check_cl3_dpi("fig.savefig('proof.png', dpi=300)").pass_)
        self.assertFalse(check_cl3_dpi("fig.savefig('proof.png', dpi=299)").pass_)

    def test_screen_profile_has_accessibility_and_integrity_rules(self) -> None:
        profile = (ROOT / "references" / "delivery-profiles.md").read_text(encoding="utf-8")
        for phrase in ("4.5:1", "3:1 contrast", "alt text", "source/method note", "1920×1080"):
            self.assertIn(phrase, profile)
        self.assertIn("must not change", profile)

    def test_review_protocol_covers_claim_image_and_context_integrity(self) -> None:
        checklist = (ROOT / "references" / "checklist.md").read_text(encoding="utf-8")
        for check_id in ("VI-8", "VI-9", "VI-10", "VV-7"):
            self.assertIn(check_id, checklist)


if __name__ == "__main__":
    unittest.main()
