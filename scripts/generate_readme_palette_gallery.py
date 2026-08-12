#!/usr/bin/env python3
"""Generate the complete two-column palette gallery in both README files."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIBRARY_PATH = ROOT / "references" / "palette-library.json"
README_SPECS = {
    "README.md": {
        "marker": "palette-gallery",
        "alt_suffix": "配色预览",
        "names": None,
    },
    "README_EN.md": {
        "marker": "palette-gallery",
        "alt_suffix": "palette preview",
        "names": {
            "nature-default": "Nature default",
            "vivid-signal": "Vivid signal",
            "bright-bio": "Bright bio",
            "teal-genome": "Teal genome",
            "muted-microbe": "Muted microbe",
            "immuno-signal": "Immuno signal",
            "pastel-catalysis": "Pastel catalysis",
            "electrochemistry": "Electrochemistry",
            "soft-cost": "Soft cost",
            "soft-academic": "Soft academic",
            "pastel-omics": "Pastel omics",
            "warm-cool-kinetics": "Warm-cool kinetics",
            "aquifer-recovery": "Aquifer recovery",
            "neuro-navy": "Neuro navy",
            "cryo-electrolyte": "Cryo electrolyte",
            "literature-clinical": "Literature clinical",
            "sage-methods": "Sage methods",
            "method-blueprint": "Method blueprint",
            "ablation-contrast": "Ablation contrast",
            "pastel-harmony": "Pastel harmony",
            "blue-red-signal": "Blue-red signal",
            "coastal-sunset": "Coastal sunset",
        },
    },
}
START = "<!-- {marker}:start -->"
END = "<!-- {marker}:end -->"


def _display_name(theme: dict[str, object], names: dict[str, str] | None) -> str:
    theme_id = str(theme["id"])
    if names is None:
        return str(theme["name"])
    if theme_id not in names:
        raise ValueError(f"Missing English display name for palette theme {theme_id!r}")
    return names[theme_id]


def build_gallery(themes: list[dict[str, object]], names: dict[str, str] | None, alt_suffix: str) -> str:
    """Build equal-width cards so the README keeps its left and right edges aligned."""
    rows = ['<table width="100%" align="center">']
    for row_index in range(0, len(themes), 2):
        cells = themes[row_index : row_index + 2]
        rows.append("  <tr>")
        for column_index, theme in enumerate(cells):
            theme_id = str(theme["id"])
            spacer = (
                '<img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt="">'
                if row_index == 0 and column_index == 0
                else ""
            )
            label = html.escape(_display_name(theme, names))
            rows.append(
                '    <td width="50%" align="center" valign="top">'
                f'{spacer}<strong>{label}</strong><br><code>{theme_id}</code><br>'
                f'<img src="assets/palette-gallery/{theme_id}.png" width="390" alt="{label} {alt_suffix}"></td>'
            )
        if len(cells) == 1:
            rows.append('    <td width="50%" align="center" valign="top">&nbsp;</td>')
        rows.append("  </tr>")
    rows.append("</table>")
    return "\n".join(rows)


def replace_gallery(readme_path: Path, gallery: str, marker: str) -> None:
    """Replace only the delimited generated block; fail instead of editing an ambiguous README."""
    start = START.format(marker=marker)
    end = END.format(marker=marker)
    text = readme_path.read_text(encoding="utf-8")
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"{readme_path.name} must contain exactly one {marker} marker pair")
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    readme_path.write_text(f"{before}{start}\n{gallery}\n{end}{after}", encoding="utf-8")


def main() -> None:
    payload = json.loads(LIBRARY_PATH.read_text(encoding="utf-8"))
    themes = payload["themes"]
    if not isinstance(themes, list) or not themes:
        raise ValueError("Palette library must contain at least one theme")
    for readme_name, spec in README_SPECS.items():
        gallery = build_gallery(themes, spec["names"], str(spec["alt_suffix"]))
        replace_gallery(ROOT / readme_name, gallery, str(spec["marker"]))
    print(f"Updated README palette galleries for {len(themes)} themes")


if __name__ == "__main__":
    main()
