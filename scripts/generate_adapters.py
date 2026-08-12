#!/usr/bin/env python3
"""Generate deterministic, truthful adapter instructions for supported coding agents."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = """# Academic Data Visualization portable rules

1. Infer the figure contract from the current request, conversation, and attachments; ask at most three task-specific, high-impact questions and state all remaining assumptions.
2. Define the claim, observation unit, data contract, and delivery profile before selecting a chart.
3. Route chart names through the canonical registry; only `production_verified + release_passed` is a release template.
4. Preserve the approved palette unless the user explicitly requests a change; add redundant non-colour encoding.
5. Execute verified templates through `scripts/run_asset.py`, never by runtime package installation or a hidden backend fallback.
6. Deliver editable SVG/PDF, exact-profile RGB and grayscale proofs, source data, metadata, alt text, and QA evidence.
7. Inspect the rendered result at final size; automated checks do not approve aesthetics.
"""


def outputs() -> dict[Path, str]:
    codex = """# Codex installation and verification

Install the complete repository under `.agents/skills/academic-data-visualization`; do not copy `SKILL.md` alone.

```bash
python -m pip install -r requirements/verified-core.txt
python scripts/check_chart_registry.py
python scripts/check_showcase_lock.py
python scripts/run_asset.py --chart-id forest-plot --demo --output-dir output/forest
```

The repository also ships `.codex-plugin/plugin.json` and a generated lightweight package under `skills/academic-data-visualization/`.

""" + CORE
    manifest = """name: academic-data-visualization
version: "2.0.0"
description: >-
  Evidence-first scientific and keynote chart selection, verified execution,
  final-size visual QA, and reproducible export.
entrypoint: SKILL.md
resources:
  - SKILL.md
  - references/
  - scripts/
  - templates/production-verified/
  - requirements/verified-core.txt
truth_model:
  runnable: production_verified
  releasable: release_passed
"""
    claude = """# Claude Code installation

Install or symlink the complete repository at `~/.claude/skills/academic-data-visualization`. Historical assets under `assets/figures/` are examples, not verified production templates.

""" + CORE
    copilot = """# GitHub Copilot repository instructions

Use the repository Skill as the source of truth. Query the registry before choosing a chart and preserve all status, data-integrity, output, and visual-review gates.

""" + CORE
    cursor = CORE + "\nRead `SKILL.md` and only the references routed for the current chart and delivery profile.\n"
    return {
        ROOT / "install" / "codex" / "instructions.md": codex,
        ROOT / "install" / "codex" / "manifest.yaml": manifest,
        ROOT / "install" / "claude-code" / "README.md": claude,
        ROOT / "install" / "copilot" / "copilot-instructions.md": copilot,
        ROOT / "install" / "cursor" / ".cursorrules": cursor,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = outputs()
    stale = [path for path, content in expected.items() if not path.is_file() or path.read_text(encoding="utf-8") != content]
    if args.check:
        for path in stale:
            print(path.relative_to(ROOT))
        raise SystemExit(1 if stale else 0)
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(expected)} adapter files")


if __name__ == "__main__":
    main()
