#!/usr/bin/env python3
"""Academic Data Visualization cross-platform adapter generator.

Reads academic-data-visualization/SKILL.md and generates platform-specific adapter files for:
  - Claude Code    (already supported via ~/.claude/skills/)
  - OpenAI Codex   (manifest.yaml)
  - Cursor         (.cursorrules)
  - GitHub Copilot (copilot-instructions.md)

Usage:
    python generate_adapters.py                    # generate all, output to install/
    python generate_adapters.py --target cursor    # generate cursor only
    python generate_adapters.py --target copilot   # generate copilot only
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = PROJECT_ROOT / "SKILL.md"
INSTALL_DIR = PROJECT_ROOT / "install"

# ═══════════════════════════════════════════════════════════
# Core rule extractor — pulls the 50-line essence from SKILL.md
# ═══════════════════════════════════════════════════════════

def extract_core_rules() -> str:
    """Extract the portable 50-line core from SKILL.md.
    These rules work across all agents — they don't depend on Claude Code's
    skill system (file loading, multi-step workflow, etc.).
    """
    with open(SKILL_MD, "r", encoding="utf-8") as f:
        full = f.read()

    # Extract flat rules: BASELINE blocks from color-palettes.md
    color_md = PROJECT_ROOT / "references" / "color-palettes.md"
    typo_md  = PROJECT_ROOT / "references" / "typography.md"
    export_md = PROJECT_ROOT / "references" / "export-specs.md"

    palette_py = _extract_code_block(color_md, "python")
    palette_r  = _extract_code_block(color_md, "r")
    typo_py    = _extract_code_block(typo_md, "python")
    typo_r     = _extract_code_block(typo_md, "r")
    export_py  = _extract_code_block(export_md, "python")

    return f'''# Academic Data Visualization Portable Core Rules
# Auto-generated from academic-data-visualization/SKILL.md — {_now()}
# These rules work across Claude Code, Codex, Cursor, and Copilot.

## Advisor Workflow
1. Define the scientific claim and unit of observation before selecting a chart.
2. Profile only the relevant sample sizes, distributions, missingness, outliers, grouping, and dependence.
3. Recommend the chart from data structure + argument; actively warn about misleading choices.
4. Fix the target journal, final physical size, panel hierarchy, and backend before plotting.
5. Render an RGB proof, run programmatic QA, inspect RGB + grayscale proofs, revise, then export.

## Design Principles
1. One figure, one core message. Remove gridlines, borders, and redundant legends.
2. Restrained color > abundant color. Use 2-4 semantic colors + 1 accent. Never default palettes.
3. Design for print, not screen. Single column 89mm, double column 183mm.
4. Vector first, raster fallback. Editable PDF/SVG/EPS for line art; TIFF/PNG (≥450dpi) for raster.
5. Never call a composite fully editable when it embeds rasterized panel images.

## Color Palette — COPY VERBATIM

```python
{palette_py}
```

```r
{palette_r}
```

Color roles: blue (#0072B2) = baseline/main evidence; bluish green (#009E73) = secondary group; orange (#E69F00) = supporting contrast; vermilion (#D55E00) = one emphasis; grey (#6B7280) = background/non-significant. Never use jet/rainbow or default matplotlib/seaborn palettes.

## Typography — COPY VERBATIM

```python
{typo_py}
```

```r
{typo_r}
```

Font: Arial/Helvetica. No text below 5pt at final print dimensions. Panel labels: lowercase bold a,b,c... at consistent positions.

## Export — COPY VERBATIM

```python
{export_py}
```

## Layout Rules
- Single column: 89mm wide. Double column: 183mm wide. Max height: 247mm.
- Remove top and right spines. Ticks outward. Gridlines off by default.
- Legend: outside plot area or direct labeling. Never inside occluding data.
- Panel width never below 35mm. Below 45mm = warn.
- Multi-panel: rows have aspect-ratio-correct heights (heatmap=1.0, ridge=0.65).

## Production Scripts
- Check `assets/figures/<type>/` and its companion preview before writing new code.
- Classify each panel as native reuse, visual adapt, or new implementation.
- Reuse only when chart semantics and data structure are compatible.
- Preserve per-panel vector masters when a mixed composite must embed raster images.
- R scripts: png(type="cairo"), showtext_auto(FALSE) before export.

## QA Checklist
- [ ] Custom hex colors used (no defaults)
- [ ] Top/right spines removed
- [ ] Arial/Helvetica font set
- [ ] Editable PDF/SVG master + 450dpi RGB PNG/TIFF proof saved
- [ ] Dimensions match journal column width
- [ ] Panel labels consistent (a,b,c...)
- [ ] Legend outside plot or direct labeling
- [ ] Colorblind-friendly (no red-green only pairs)
- [ ] RGB and grayscale proofs inspected at intended size
- [ ] Rasterized composite panels disclosed
'''


def _extract_code_block(path: Path, language: str) -> str:
    """Extract the first fenced code block for the given language from a markdown file."""
    if not path.exists():
        return f"# {language} block not found"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Match ```language ... ```  (language can be python or r)
    pattern = rf"```\s*{language}\s*\n(.*?)```"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return f"# No {language} block found in {path.name}"


def _now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# ═══════════════════════════════════════════════════════════
# Platform generators
# ═══════════════════════════════════════════════════════════

def generate_claude_code(core: str) -> str:
    """Claude Code: already supported via ~/.claude/skills/. This generates a README."""
    return f'''# Academic Data Visualization — Claude Code Installation

The Claude Code skill is at `academic-data-visualization/`. Install via symlink:

```bash
ln -s $(pwd)/academic-data-visualization ~/.claude/skills/academic-data-visualization
```

Or copy:
```bash
cp -r academic-data-visualization ~/.claude/skills/academic-data-visualization
```

After installation, Claude Code auto-triggers on: "make a volcano plot", "画个热图",
"review this figure for Nature", etc.

The skill checks `academic-data-visualization/assets/figures/<type>/` for production scripts before
generating any code. Add your own scripts there to extend figure type coverage.

Generated: {_now()}
'''


def generate_codex_manifest(core: str) -> str:
    """OpenAI Codex: needs a manifest.yaml + instructions.md bundle."""
    manifest = f'''# Academic Data Visualization — OpenAI Codex Manifest
# Place this file at: ~/.codex/skills/academic-data-visualization/manifest.yaml
# Generated: {_now()}

name: academic-data-visualization
version: "1.0.0"
description: >-
  Publication-grade scientific figure advising, creation, revision, and visual QA.
  Profiles data, selects defensible charts, applies journal-aware layout and colour,
  and exports reproducible Python/R figures.

entrypoint: SKILL.md
resources:
  - SKILL.md
  - instructions.md
  - references/
  - scripts/
  - assets/figures/

triggers:
  - keywords: [figure, plot, chart, heatmap, volcano, boxplot, scatter, bar,
               manuscript, publication, Nature, Cell, Science,
               论文配图, 科研绘图, 学术图表, 图, 绘图, 作图]
  - file_patterns: ["*.py", "*.R", "*.r"]
    content_hints: ["matplotlib", "ggplot2", "seaborn", "ComplexHeatmap",
                    "plt.plot", "plt.scatter", "ggplot(", "geom_"]
'''

    instructions = f'''# Academic Data Visualization Instructions for Codex
# Auto-generated from academic-data-visualization/SKILL.md — {_now()}

{core}
'''
    return manifest, instructions


def generate_cursor_rules(core: str) -> str:
    """Cursor: inject as .cursorrules in the user's project root."""
    # Cursor uses .cursorrules for project-level AI instructions
    return f'''# Academic Data Visualization — Scientific Figure Making Rules
# Place this file at: <your-project>/.cursorrules
# Cursor auto-loads it. Generated: {_now()}

You are helping create scientific figures for Nature/Cell/Science journals.
Follow these rules when writing matplotlib/ggplot2/ComplexHeatmap code.

{core}
'''


def generate_copilot_instructions(core: str) -> str:
    """GitHub Copilot: inject as .github/copilot-instructions.md."""
    return f'''# Academic Data Visualization — Scientific Figure Instructions for GitHub Copilot
# Place this file at: <your-repo>/.github/copilot-instructions.md
# Generated: {_now()}

{core}
'''


# ═══════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════

TARGETS = {
    "claude-code": "Claude Code (README)",
    "codex": "OpenAI Codex (manifest + instructions)",
    "cursor": "Cursor (.cursorrules)",
    "copilot": "GitHub Copilot (copilot-instructions.md)",
}


def generate(target: str | None = None):
    """Generate adapters. If target is None, generate all."""
    core = extract_core_rules()

    targets_to_build = [target] if target else list(TARGETS)
    for t in targets_to_build:
        if t not in TARGETS:
            print(f"Unknown target: {t}. Choose from: {', '.join(TARGETS)}")
            sys.exit(1)

    print(f"Academic Data Visualization Adapter Generator — {_now()}")
    print(f"Source: {SKILL_MD}")
    print()

    for t in targets_to_build:
        out_dir = INSTALL_DIR / t
        out_dir.mkdir(parents=True, exist_ok=True)

        if t == "claude-code":
            readme = generate_claude_code(core)
            path = out_dir / "README.md"
            path.write_text(readme, encoding="utf-8")
            print(f"[OK] {t} → {path}")

        elif t == "codex":
            manifest, instructions = generate_codex_manifest(core)
            (out_dir / "manifest.yaml").write_text(manifest, encoding="utf-8")
            (out_dir / "instructions.md").write_text(instructions, encoding="utf-8")
            print(f"[OK] {t} → {out_dir}/manifest.yaml + instructions.md")

        elif t == "cursor":
            rules = generate_cursor_rules(core)
            path = out_dir / ".cursorrules"
            path.write_text(rules, encoding="utf-8")
            print(f"[OK] {t} → {path}")

        elif t == "copilot":
            instructions = generate_copilot_instructions(core)
            path = out_dir / "copilot-instructions.md"
            path.write_text(instructions, encoding="utf-8")
            print(f"[OK] {t} → {path}")

    print(f"\nAll generated under: {INSTALL_DIR}")
    print("Copy the relevant file(s) to your project/agent directory.")


if __name__ == "__main__":
    target = None
    if "--target" in sys.argv:
        idx = sys.argv.index("--target")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]
    generate(target)
