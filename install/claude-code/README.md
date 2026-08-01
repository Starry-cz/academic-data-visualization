# Claude Code installation

Install or symlink the complete repository at `~/.claude/skills/academic-data-visualization`. Historical assets under `assets/figures/` are examples, not verified production templates.

# Academic Data Visualization portable rules

1. Define the claim, observation unit, data contract, and delivery profile before selecting a chart.
2. Route chart names through the canonical registry; only `production_verified + release_passed` is a release template.
3. Preserve the approved palette unless the user explicitly requests a change; add redundant non-colour encoding.
4. Execute verified templates through `scripts/run_asset.py`, never by runtime package installation or a hidden backend fallback.
5. Deliver editable SVG/PDF, exact-profile RGB and grayscale proofs, source data, metadata, alt text, and QA evidence.
6. Inspect the rendered result at final size; automated checks do not approve aesthetics.
