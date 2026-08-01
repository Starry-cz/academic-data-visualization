# Repository agent instructions

## Architecture and truth model

- Keep `SKILL.md` as the decision entry point; detailed chart knowledge belongs in `references/`.
- Treat `references/chart-registry.yaml` as the canonical chart knowledge registry and each `asset.yaml` as the execution truth for one asset.
- Use the v2 axes independently: `knowledge_status`, `implementation_status`, and `verification_status`.
- Only `production_verified + release_passed` may be routed through `scripts/run_asset.py` as a release template.
- `legacy_example`, `pattern`, and `none` are not production states. Never infer a stronger state from the presence of a PNG or script.
- Preserve public paths, all historical examples, the approved 24-card README gallery, and the existing palette library.

## Production gate

A production asset must have all of the following:

1. Manifest v2 with an explicit entrypoint, environment, data contract, output contract, safety policy, provenance, and verification evidence.
2. The unified `--input/--demo/--output-dir/--profile/--theme/--seed` interface.
3. No runtime package installation, network access, hidden fallback backend, or writes outside the selected output directory.
4. Passing demo and checked-fixture executions from a clean temporary directory.
5. Editable SVG/PDF, exact-profile RGB PNG, grayscale proof, source data, metadata, alt text, QA report, and run record.
6. Programmatic output QA, stored hashes, and final-size visual review recorded in `verification-record.json`.

If any gate fails, keep the asset at `demo_runnable`, `legacy_example`, or a lower state and report the exact blocker.

## Generated and protected files

- Do not hand-edit `references/chart-types/*.md`, `references/chart-alias-index.md`, `references/chart-registry-stats.json`, or `references/directory-map.md`.
- Regenerate catalogue files with `python scripts/generate_chart_catalog.py`.
- Regenerate the asset directory with `python scripts/generate_directory_map.py`.
- Build the plugin Skill package with `python scripts/build_skill_package.py`; CI checks for drift.
- `references/showcase-lock.json` protects the maintainer-approved README figures and palette assets. Refresh it only after explicit maintainer approval.
- `scripts/migrate_registry_v2.py` is a one-time migration utility, not a routine build command.

## Code style

- 添加必要的中文注释，解释非显然的统计、路由、安全与布局决策。
- 尽量避免兜底代码；输入、依赖、字体、数据契约或语义不满足时明确失败。
- Keep standard-library-only tools dependency-free. Production rendering dependencies belong in `requirements/verified-core.txt`.
- Never install Python or R packages from inside a plotting script.

## Required checks

```bash
python scripts/check_skill_metadata.py
python scripts/check_references.py
python scripts/check_chart_registry.py
python scripts/build_chart_registry.py --check
python scripts/generate_chart_catalog.py --check
python scripts/generate_directory_map.py --check
python scripts/check_showcase_lock.py
python scripts/build_skill_package.py --check
python -m unittest discover -s tests -v
python scripts/trigger_benchmark.py
python scripts/qa_coverage.py
python scripts/verify_production_assets.py
python -m compileall -q scripts assets/figures templates tests
```

R examples must also parse in CI. Absence of a local R runtime is not permission to mark them verified.

## Git and data safety

- Do not overwrite user data or reuse a non-empty output directory without explicit `--overwrite`.
- Do not use destructive reset, force-push, or destructive checkout commands.
- Do not commit local absolute paths, private attachment names, temporary directories, caches, or credentials.
- Do not fabricate data, previews, evidence, hashes, manual review, or production status.
