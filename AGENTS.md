# Repository agent instructions

## Architecture

- Keep `SKILL.md` concise; detailed chart knowledge belongs in `references/`.
- Treat `references/chart-registry.yaml` as the single source of truth for chart taxonomy.
- Keep `references/directory-map.md` limited to real production asset directories.
- Never claim a chart is production-ready unless its script, PNG, and `asset.yaml` exist and pass validation.
- Preserve existing public paths and the six atlas groups.

## Generated files

- Do not hand-edit `references/chart-types/*.md`, `references/chart-alias-index.md`, or `references/chart-registry-stats.json`.
- Regenerate them with `python scripts/generate_chart_catalog.py`.
- Regenerate production manifests with `python scripts/build_chart_registry.py --sync-manifests`.

## Code style

- 添加必要的中文注释，解释非显然的统计、路由和布局决策。
- 尽量避免兜底代码；输入、依赖或语义不满足时应明确失败。
- Do not add external Python dependencies when the standard library is sufficient.

## Required checks

- `python scripts/check_skill_metadata.py`
- `python scripts/check_references.py`
- `python scripts/check_chart_registry.py`
- `python scripts/build_chart_registry.py --check`
- `python scripts/generate_chart_catalog.py --check`
- `python -m unittest discover -s tests -v`
- `python scripts/trigger_benchmark.py`
- `python scripts/qa_coverage.py`
- `python -m compileall -q scripts assets/figures tests`

## Safety

- Do not overwrite user data.
- Do not use `git reset --hard`, force-push, or destructive checkout commands.
- Do not fabricate previews or production status for unimplemented charts.
