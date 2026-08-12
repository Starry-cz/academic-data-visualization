from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ClarificationGateTests(unittest.TestCase):
    def test_skill_requires_context_adaptive_questions(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        required = (
            "current request, earlier turns, attached data or images",
            "highest-impact **one to three** questions",
            "generated for this request rather than copied from a fixed questionnaire",
            "Ask zero questions when the context is already sufficient",
            "Assumptions",
        )
        for phrase in required:
            self.assertIn(phrase, text)

    def test_contract_caps_questions_and_protects_scientific_facts(self) -> None:
        text = (ROOT / "references" / "figure-contract.md").read_text(encoding="utf-8")
        required = (
            "known / inferred / unresolved",
            "no more than **three** questions",
            "do not reuse a fixed list",
            "Do not ask for information already stated",
            "Never default or infer scientific facts",
            "identify the exact blocker instead of fabricating it",
        )
        for phrase in required:
            self.assertIn(phrase, text)

    def test_portable_adapters_keep_the_dynamic_gate(self) -> None:
        text = (ROOT / "scripts" / "generate_adapters.py").read_text(encoding="utf-8")
        self.assertIn("current request, conversation, and attachments", text)
        self.assertIn("at most three task-specific, high-impact questions", text)
        self.assertIn("state all remaining assumptions", text)


if __name__ == "__main__":
    unittest.main()
