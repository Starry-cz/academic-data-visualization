# Claude Code installation

Install or symlink the complete repository at `~/.claude/skills/academic-data-visualization`. Historical assets under `assets/figures/` are examples, not verified production templates.

# Academic Data Visualization portable rules

1. Infer the figure contract from the current request, conversation, and attachments; ask at most three task-specific, high-impact questions and state all remaining assumptions.
2. Define the claim, observation unit, data contract, and delivery profile before selecting a chart.
3. Route chart names through the canonical registry; only `production_verified + release_passed` is a release template.
4. Preserve the approved palette unless the user explicitly requests a change; add redundant non-colour encoding.
5. Execute verified templates through `scripts/run_asset.py`, never by runtime package installation or a hidden backend fallback.
6. Deliver editable SVG/PDF, exact-profile RGB and grayscale proofs, source data, metadata, alt text, and QA evidence.
7. Inspect the rendered result at final size; automated checks do not approve aesthetics.
