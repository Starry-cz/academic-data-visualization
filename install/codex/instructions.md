# Codex installation and verification

Install the complete repository under `.agents/skills/academic-data-visualization`; do not copy `SKILL.md` alone.

```bash
python -m pip install -r requirements/verified-core.txt
python scripts/check_chart_registry.py
python scripts/check_showcase_lock.py
python scripts/run_asset.py --chart-id forest-plot --demo --output-dir output/forest
```

The repository also ships `.codex-plugin/plugin.json` and a generated lightweight package under `skills/academic-data-visualization/`.

# Academic Data Visualization portable rules

1. Define the claim, observation unit, data contract, and delivery profile before selecting a chart.
2. Route chart names through the canonical registry; only `production_verified + release_passed` is a release template.
3. Preserve the approved palette unless the user explicitly requests a change; add redundant non-colour encoding.
4. Execute verified templates through `scripts/run_asset.py`, never by runtime package installation or a hidden backend fallback.
5. Deliver editable SVG/PDF, exact-profile RGB and grayscale proofs, source data, metadata, alt text, and QA evidence.
6. Inspect the rendered result at final size; automated checks do not approve aesthetics.
