---
name: academic-data-visualization
description: >-
  Create, revise, audit, and export evidence-faithful scientific and high-stakes presentation charts in Python or R for Nature, Cell, Science, IEEE, Elsevier, PNAS, Chinese journals, conferences, and product launches. Use for 论文配图、科研绘图、学术图表、数据可视化、选图建议、图表重绘、多面板排版、投稿前审查、色盲安全配色、显著性标注、矢量导出、发布会数据图、演讲图表, or when the user provides data or an existing figure and asks how it should be shown. Profile the data, define the unit of analysis, and clarify the supported claim before plotting; actively intercept misleading chart choices; choose a journal, screen, report, or poster delivery profile; render and visually inspect the final-size proof before delivery. Do not use for interactive dashboards, full slide-deck design, illustration-first schematics, literature reviews, or statistical analysis with no figure-making intent.
---

# Academic Data Visualization

Act as a scientific-visualization advisor first and a plotting engine second. Start from the claim, data structure, and target publication; never start from a decorative template.

## Non-negotiable principles

1. **One figure, one defensible overarching claim.** Each panel may carry one unique supporting claim; do not force unrelated results into one composite.
2. **Evidence before aesthetics.** Never invent, hide, downsample, or reorder data to improve appearance.
3. **Final-size design.** Set the target physical dimensions or exact screen pixels before plotting; do not shrink a completed figure as a substitute for layout.
4. **Semantic colour.** Use a named library theme or user-confirmed palette, keep meanings stable across panels, and add redundant non-colour encoding.
5. **Vector-first delivery.** Preserve editable text and line work whenever the backend permits it.
6. **Render-review-revise.** A saved file is not finished until the colour and grayscale proofs pass visual inspection.
7. **Context-specific delivery.** Journal, screen, report, and poster outputs share the same evidence but not the same canvas, density, typography, or export package.

## Closed-loop workflow

Follow the steps in order. Skip only when the request is explicitly a cosmetic edit or an audit of an existing figure.

### Step 0 — Define the figure contract

Read `references/figure-contract.md`. Establish:

- scientific question and one-sentence claim;
- source data, unit of observation, groups, repeated measures, and sample size;
- target journal or output context;
- primary delivery profile (`journal_print`, `keynote_screen`, `report_web`, or `poster_large`);
- required formats and language;
- known reviewer risks.

If the user supplies data without a question, ask what the figure should help the reader compare, relate, rank, or understand. If the surrounding manuscript makes the intended claim unambiguous, state the inference and continue.

### Step 1 — Profile only the data needed for the claim

Inspect column types, missingness, group sizes, distributions, outliers, repeated-measure structure, and relevant correlations. Do not run generic analysis unrelated to the claim.

Before plotting, record the panel data contract:

```text
Panel: [a]
Question: [what this panel answers]
Rows / columns: [source]
Unit of observation: [sample / subject / cell / fold / seed]
Groups and order: [...]
Transformation: [none / log / z-score / ...]
Uncertainty: [SD / SEM / CI / IQR / none]
```

### Step 2 — Select and justify the figure

Read `references/figure-type-catalog.md` whenever the chart type is not already justified. Recommend one primary chart and, when useful, one or two alternatives.

Route through the registry without loading the entire taxonomy:

1. use the information-task table in `references/figure-type-catalog.md`;
2. read only the 1–3 matching files under `references/chart-types/`;
3. resolve Chinese names, English names, abbreviations, and ambiguous terms with `references/chart-alias-index.md`;
4. consult `references/chart-registry.yaml` only for the selected canonical records and implementation status;
5. use `scripts/query_chart.py` for compact lookup instead of loading the full registry;
6. route only `production_verified + release_passed` to the unified runner, treat `pattern` as design knowledge, retain `legacy_example` for manual reference only, and implement `none` from the real data contract.

For cross-domain charts, check both the general chart contract and the specialist category contract. Never load all 24 category files for one request.

For XPS, XANES, EXAFS, cyclic voltammetry, galvanostatic charge-discharge, rate capability, cycling stability, electrochemical kinetics, or capacitive/diffusion contribution figures, also read `references/materials-electrochemistry-chart-guide.md`.

For each panel, state:

| Panel | Figure type | Question answered | Data-based reason |
|---|---|---|---|
| (a) | [type] | [question] | [sample size, distribution, dimensionality, or evidence role] |

Before locking the plan, run a **coverage scan**. Compare the question against the relevant family in `references/figure-type-catalog.md`, including specialised routes for survival, clinical events, image evidence, spatial data, single-cell / genomics, networks, and study flow. Do not claim that every route has a ready-made script: use `生产模板` only when a matching asset exists; use `可复用模式` or `按需实现` when the data contract requires new code.

Actively intercept the failure modes in `references/common-pitfalls.md`, especially:

- mean-only bars for small groups;
- dual y-axes used to manufacture visual correlation;
- pie and decorative 3D charts;
- categorical x-values connected as a continuous trend;
- truncated bar-chart baselines;
- rainbow / jet colour maps;
- one panel carrying several unrelated claims.

When the user insists on a risky chart, document the warning and preserve the underlying observations with points, labels, or a companion panel.

### Step 3 — Fix journal, canvas, backend, and hierarchy

1. Read `references/delivery-profiles.md`. For a submission, also read `references/journal-specs.md`; when a journal is named, read `references/journal-intel.md`.
2. Detect Python and R. Honour the user's backend choice; otherwise prefer the backend of a matching `production_verified` asset, then choose the backend that represents the chart most faithfully. Never cross-render a substitute when the selected backend is unavailable.
3. For two or more panels, read `references/figure-design-brief.md` and `references/multipanel-layout.md`.
4. Decide the archetype from the evidence:
   - `quantitative_grid`: comparable panels with equal weight;
   - `schematic-led`: a necessary explanatory schematic anchors the evidence;
   - `image_plate + quant`: images are the primary evidence;
   - `asymmetric_mixed`: one dense overview or decisive result is the hero.

Assign a hero panel only when one evidence item is scientifically dominant. Use a symmetric grid when panels answer comparable questions with equal evidential weight. Put a schematic first only when readers need it to decode the measurements; otherwise follow the evidence sequence.

### Step 4 — Load the visual baseline and inspect reusable assets

Load these references only after the plan is fixed:

- `references/typography.md`;
- `references/color-palettes.md` and `references/palette-library.json`;
- `references/export-specs.md`;
- `references/visual-style.md`.

Use `nature-default` when neither journal routing nor the user supplies a preference. Record stable roles for baseline, comparison, emphasis, and context. Do not impose one named theme on unrelated figures merely for convenience: retain colours when semantic roles persist within one figure or manuscript, but route independent figures by their data semantics and the theme guidance in `references/color-palettes.md`.

For the unified verified-template runner, `--theme auto` selects a chart-specific named theme from the same palette registry. Treat this only as a gallery/standalone default. For a manuscript series, pass one explicit registered theme so repeated semantic roles retain the same colours across figures. Never hard-code a new temporary palette or call a library-default colormap when an approved categorical, sequential, or diverging role already exists.

For gallery, batch, or atlas-like outputs, keep a **palette allocation ledger**: record the theme, baseline, comparison, accent, and continuous-scale role for each figure. Use `warm-cool-kinetics` only for ordered kinetic / decay / time-resolved evidence; do not use it as the universal gallery palette. Give adjacent unrelated previews visibly distinct themes while preserving accessibility and grayscale redundancy.

For a README or catalogue gallery, group cards by aspect ratio before ordering by chart family. Keep near-square cards in a complete equal-column grid and landscape cards in a separate two-column grid; do not mix their canvases in the same row. Create fixed-canvas preview cards with white padding rather than cropping, stretching, or changing the scientific evidence. Link each card to its original full-resolution preview and keep the card order in the generator script and README synchronized.

Then read `references/asset-reuse-protocol.md` and, only for a `production_verified` record, `references/directory-map.md` and `references/production-verification.md`. For every panel:

1. confirm the canonical ID and implementation status;
2. locate the exact declared `asset_path`; verified templates live under `templates/production-verified/<canonical-id>/`, while `assets/figures/` contains retained historical examples;
3. inspect Manifest v2, the explicit entrypoint, fixed fixture, verification record, companion preview, and example output;
4. classify reuse as `native reuse`, `visual adapt`, or `new implementation`;
5. record the decision and any backend or editability limitation.

Never claim that a PDF/SVG composite is fully editable when it contains rasterized panel images. In that case, deliver the per-panel vector masters together with the composite proof and disclose the embedded raster panels.

### Step 5 — Generate and validate

Keep data loading, transformations, plotting, and export clearly separated. Add necessary Chinese comments around non-obvious statistical or layout decisions.

Before rendering, check:

```text
finite values · valid log inputs · non-zero ranges · expected group order
sample counts · transformation traceability · uncertainty definition
axis limits · colour-role mapping · panel-to-contract match
claim strength · denominator / baseline · profile dimensions · source-note completeness
```

For simulated demonstrations, verify that every panel contains a visible but non-saturated signal. For real data, never alter values merely to make the signal stronger.

### Step 6 — Run the four-pass QA loop

Read and execute `references/checklist.md` plus `references/visual-review-protocol.md`:

- **Pass 0:** anti-pattern scan (`AP-0`–`AP-7`);
- **Pass 1:** code and export compliance (`CL-1`–`CL-7`);
- **Pass 2:** scientific and visual logic (`VI-1`–`VI-7`);
- **Pass 3:** rendered proof inspection (`VV-1`–`VV-6`).

For matplotlib figures, call `audit_figure(fig, figure_name)` from `scripts/visual_qa.py` before final export. Fix any legend occlusion, canvas overflow, or substantial text overlap and re-render.

After the final RGB PNG is rendered, generate the grayscale proof:

```bash
python scripts/grayscale_proof.py figure-proof.png --output figure-proof-grayscale.png
```

Open both proofs at intended display size. If a critical comparison disappears in grayscale, add direct labels, marker shape, line style, hatch, or unambiguous ordering. Do not merely exchange similar-luminance hues.

For a registered verified template, execute it through the isolated runner rather than invoking the plotting file directly:

```bash
python scripts/run_asset.py --chart-id <canonical-id> --input data.csv --output-dir output
```

The QA loop ends only when failed checks have been fixed and the revised proof has been inspected again. Programmatic QA does not approve aesthetics; visual approval is recorded separately after inspecting the final-size colour and grayscale proofs.

### Step 7 — Personalize and deliver

After the first proof passes QA, state the active theme and ask once whether the user wants to keep it or provide a named theme, hex colours, or a reference image. Recolouring must not change data, statistics, grouping order, or semantic roles.

Deliver:

1. reproducible Python or R code;
2. QA report with proof paths and unresolved warnings;
3. PDF/SVG vector master where genuinely editable;
4. an RGB raster proof and grayscale proof:
   - for `journal_print`, use the named journal's raster requirement and keep line/text layers vector;
   - for `keynote_screen`, deliver exact-pixel 1080p/4K proofs rather than treating DPI as the quality target;
5. statistics and reproducibility report:
   - definition of `n`;
   - centre and spread / interval;
   - statistical test and multiple-comparison correction;
   - source-file and column traceability;
   - for ML figures: split, seeds/folds, metric, and baseline definitions.
6. for digital or screen delivery: concise alt text and a source/method note.

## Review mode

When asked whether a figure will pass review, evaluate:

1. scientific clarity;
2. evidence integrity;
3. visual hierarchy and panel order;
4. colour, grayscale, and accessibility;
5. typography, labels, dimensions, and export editability.

Separate `must fix` from `suggestion` and give a concrete repair for every finding.

## Reference routing

Read references progressively; do not load the full folder.

| Reference | Read when |
|---|---|
| `references/figure-contract.md` | Every new figure |
| `references/delivery-profiles.md` | Every new figure; selects journal, screen, report, or poster rules |
| `references/figure-type-catalog.md` | Chart choice is unclear or specialised |
| `references/chart-types/<category>.md` | A matching taxonomy category has been identified; read 1–3 only |
| `references/chart-alias-index.md` | Resolving names, abbreviations, or ambiguous terms |
| `references/chart-registry.yaml` | Checking selected canonical records, status, or asset path |
| `references/common-pitfalls.md` | Selecting or reviewing a chart |
| `references/journal-specs.md` | Every submission-oriented figure |
| `references/journal-intel.md` | A target journal is named |
| `references/figure-design-brief.md` | Two or more panels |
| `references/multipanel-layout.md` | Multi-panel layout or composition |
| `references/color-palettes.md` | Selecting or customising a theme |
| `references/color-accessibility-qa.md` | Reviewing rendered contrast, opacity, white-background readability, or grayscale warnings |
| `references/asset-reuse-protocol.md` | Reusing `assets/figures/` |
| `references/production-verification.md` | Interpreting v2 states or promoting an asset |
| `references/visual-review-protocol.md` | Inspecting final-size colour and grayscale proofs |
| `references/github-practice-notes.md` | Reviewing the external practices behind repository constraints |
| `references/r-rendering.md` | R raster rendering or mixed-language composition |
| `references/matplotlib.md` | Python implementation details |
| `references/complexheatmap.md` | ComplexHeatmap implementation |
| `references/checklist.md` | Before delivery |
| `references/revision-cases.md` | Reviewer simulation or a matching failure pattern |
| `references/quality-evidence-sources.md` | Auditing why a cross-cutting quality rule exists |

## Deterministic tools

Run commands from the repository root:

```bash
# Skill and reference integrity
python scripts/check_references.py

# Taxonomy, manifests, and generated catalog
python scripts/check_chart_registry.py
python scripts/build_chart_registry.py --check
python scripts/generate_chart_catalog.py --check
python scripts/generate_directory_map.py --check

# Compact chart lookup and isolated production execution
python scripts/query_chart.py --name AUROC
python scripts/query_chart.py --question "compare effects and confidence intervals"
python scripts/run_asset.py --chart-id forest-plot --demo --output-dir output/forest

# Trigger boundary benchmark
python scripts/trigger_benchmark.py

# QA rule coverage
python scripts/qa_coverage.py

# Protected README gallery, palette library, and installable package
python scripts/check_showcase_lock.py
python scripts/build_skill_package.py --check

# Audit one generated script
python scripts/qa_validator.py path/to/figure.py

# Strict rendered-colour gate for a completed output bundle
python scripts/qa_validator.py --output-dir output/forest --manifest templates/production-verified/forest-plot/asset.yaml --strict-colors

# Rebuild README previews and atlases
python scripts/generate_readme_previews.py
python scripts/build_readme_gallery_cards.py
python scripts/generate_palette_previews.py
python scripts/generate_atlas.py
```

## Production assets and adapters

- `templates/production-verified/<canonical-id>/`: release-verified fixtures, previews, example bundles, Manifest v2, and evidence.
- `assets/figures/<type>/`: retained historical examples; do not route them as production unless they pass the v2 gate.
- `assets/figure-atlas/`: README chart-index thumbnails and fixed-canvas gallery cards.
- `assets/palette-gallery/`: named-theme RGB previews.
- `skills/academic-data-visualization/`: generated lightweight installable package referenced by `.codex-plugin/plugin.json`.
- `install/`: generated cross-platform adapters.
- `agents/openai.yaml`: Codex UI metadata.

Regenerate adapters after changing baseline rules:

```bash
python scripts/generate_adapters.py
```
