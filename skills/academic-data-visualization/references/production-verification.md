# Production Verification Contract

## Status model

Keep knowledge coverage, implementation maturity, and verification evidence separate.

| Dimension | Values | Meaning |
|---|---|---|
| Knowledge | `registered`, `reviewed`, `deprecated` | Whether the chart guidance itself has been reviewed |
| Implementation | `none`, `pattern`, `legacy_example`, `demo_runnable`, `production_verified`, `deprecated` | What executable asset actually exists |
| Verification | `untested`, `syntax_parsed`, `rendered_passed`, `release_passed`, `failed` | Strength of current evidence |

Never infer one dimension from another. A preview does not prove an implementation, and syntax parsing does not prove execution.

## Production gate

Mark an asset `production_verified` only when all conditions below are evidenced:

1. Declare one explicit production entrypoint and interface version.
2. Declare a versioned input contract, missing-value policy, and minimum sample requirement.
3. Execute deterministic demo data and a checked-in validation fixture.
4. Run without network access or runtime package installation.
5. Resolve input and output paths independently of the current working directory.
6. Refuse overwrites by default and write only inside the requested output directory.
7. Produce editable PDF and SVG, RGB PNG, grayscale proof, metadata, alt text, and source data.
8. Open and validate the actual output files; do not infer delivery quality from source strings.
9. Record input hashes, output hashes, package versions, runner version, and QA version.
10. Complete the scientific and perceptual review rubric in `visual-review-protocol.md`.
11. Pass the repository CI execution lane.
12. Record code, data, and third-party asset provenance.

If any condition is missing, use `demo_runnable` or `legacy_example` instead.

## Unified command

Run a verified asset through the repository runner:

```bash
python scripts/run_asset.py \
  --chart-id forest-plot \
  --input results.csv \
  --output-dir output/forest \
  --profile journal_print \
  --theme auto
```

Use `--demo` instead of `--input` for deterministic demonstration data. `--theme auto` routes the chart to a named theme already present in `references/palette-library.json`; pass any registered theme ID to override it. The renderer records the resolved theme and all four colour roles, and QA rejects output whose values do not exactly match the registry. Do not pass `--overwrite` unless the target directory was explicitly chosen for replacement.

The chart-specific defaults are an allocation ledger for independent examples, not a new palette library. They never edit registered hex values. Within one manuscript, override `auto` with a single appropriate named theme whenever category semantics must remain stable across figures.

## Evidence semantics

- `syntax_parsed`: the source parser accepted the entrypoint. It was not executed.
- `rendered_passed`: the entrypoint ran and created structurally valid files, but release evidence is incomplete.
- `release_passed`: both data modes, output QA, provenance, hashes, and manual review are recorded.

Never use “verified,” “production-ready,” or “release-ready” for the first two states.
