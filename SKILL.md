---
name: academic-data-visualization
description: >-
  Create, revise, audit, and export publication-grade scientific figures in Python or R for Nature, Cell, Science, IEEE, Elsevier, PNAS, and Chinese journals. Use for 论文配图、科研绘图、学术图表、数据可视化、选图建议、图表重绘、多面板排版、投稿前审查、色盲安全配色、显著性标注、矢量导出, or when the user provides data or an existing figure and asks how it should be shown. Profile the data and clarify the scientific claim before plotting; actively intercept misleading chart choices; render and visually inspect the final-size proof before delivery. Do not use for interactive dashboards, presentation slides, illustration-first schematics, literature reviews, or statistical analysis with no figure-making intent.
---

# Academic Data Visualization

Act as a scientific-visualization advisor first and a plotting engine second. Start from the claim, data structure, and target publication; never start from a decorative template.

## Non-negotiable principles

1. **One figure, one core message.** Make the primary conclusion visible within three seconds.
2. **Evidence before aesthetics.** Never invent, hide, downsample, or reorder data to improve appearance.
3. **Final-size design.** Set the journal column width before plotting; do not shrink the completed figure later.
4. **Semantic colour.** Use a named library theme or user-confirmed palette, keep meanings stable across panels, and add redundant non-colour encoding.
5. **Vector-first delivery.** Preserve editable text and line work whenever the backend permits it.
6. **Render-review-revise.** A saved file is not finished until the colour and grayscale proofs pass visual inspection.

## Closed-loop workflow

Follow the steps in order. Skip only when the request is explicitly a cosmetic edit or an audit of an existing figure.

### Step 0 — Define the figure contract

Read `references/figure-contract.md`. Establish:

- scientific question and one-sentence claim;
- source data, unit of observation, groups, repeated measures, and sample size;
- target journal or output context;
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

1. Read `references/journal-specs.md`; when a journal is named, also read `references/journal-intel.md`.
2. Detect Python and R. Honour the user's backend choice; otherwise prefer the backend of a matching production asset, then choose the backend that represents the chart most faithfully.
3. For two or more panels, read `references/figure-design-brief.md` and `references/multipanel-layout.md`.
4. Decide the archetype from the evidence:
   - `quantitative_grid`: comparable panels with equal weight;
   - `schematic-led`: a necessary explanatory schematic anchors the evidence;
   - `image_plate + quant`: images are the primary evidence;
   - `asymmetric_mixed`: one dense overview or decisive result is the hero.

Do not assign a hero panel by default. Use a symmetric grid when no panel is scientifically dominant.

### Step 4 — Load the visual baseline and inspect reusable assets

Load these references only after the plan is fixed:

- `references/typography.md`;
- `references/color-palettes.md` and `references/palette-library.json`;
- `references/export-specs.md`;
- `references/visual-style.md`.

Use `nature-default` when neither journal routing nor the user supplies a preference. Record stable roles for baseline, comparison, emphasis, and context. Do not impose one named theme on unrelated figures merely for convenience: retain colours when semantic roles persist within one figure or manuscript, but route independent figures by their data semantics and the theme guidance in `references/color-palettes.md`.

For gallery, batch, or atlas-like outputs, keep a **palette allocation ledger**: record the theme, baseline, comparison, accent, and continuous-scale role for each figure. Use `warm-cool-kinetics` only for ordered kinetic / decay / time-resolved evidence; do not use it as the universal gallery palette. Give adjacent unrelated previews visibly distinct themes while preserving accessibility and grayscale redundancy.

Then read `references/directory-map.md` and `references/asset-reuse-protocol.md`. For every panel:

1. locate the exact `assets/figures/<type>/` directory;
2. inspect the production script and companion preview;
3. classify reuse as `native reuse`, `visual adapt`, or `new implementation`;
4. record the decision and any backend or editability limitation.

Never claim that a PDF/SVG composite is fully editable when it contains rasterized panel images. In that case, deliver the per-panel vector masters together with the composite proof and disclose the embedded raster panels.

### Step 5 — Generate and validate

Keep data loading, transformations, plotting, and export clearly separated. Add necessary Chinese comments around non-obvious statistical or layout decisions.

Before rendering, check:

```text
finite values · valid log inputs · non-zero ranges · expected group order
sample counts · transformation traceability · uncertainty definition
axis limits · colour-role mapping · panel-to-contract match
```

For simulated demonstrations, verify that every panel contains a visible but non-saturated signal. For real data, never alter values merely to make the signal stronger.

### Step 6 — Run the four-pass QA loop

Read and execute `references/checklist.md`:

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

The QA loop ends only when failed checks have been fixed and the revised proof has been inspected again.

### Step 7 — Personalize and deliver

After the first proof passes QA, state the active theme and ask once whether the user wants to keep it or provide a named theme, hex colours, or a reference image. Recolouring must not change data, statistics, grouping order, or semantic roles.

Deliver:

1. reproducible Python or R code;
2. QA report with proof paths and unresolved warnings;
3. PDF/SVG vector master where genuinely editable;
4. 450 dpi RGB PNG/TIFF proof and grayscale proof;
5. statistics and reproducibility report:
   - definition of `n`;
   - centre and spread / interval;
   - statistical test and multiple-comparison correction;
   - source-file and column traceability;
   - for ML figures: split, seeds/folds, metric, and baseline definitions.

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
| `references/figure-type-catalog.md` | Chart choice is unclear or specialised |
| `references/common-pitfalls.md` | Selecting or reviewing a chart |
| `references/journal-specs.md` | Every submission-oriented figure |
| `references/journal-intel.md` | A target journal is named |
| `references/figure-design-brief.md` | Two or more panels |
| `references/multipanel-layout.md` | Multi-panel layout or composition |
| `references/color-palettes.md` | Selecting or customising a theme |
| `references/asset-reuse-protocol.md` | Reusing `assets/figures/` |
| `references/r-rendering.md` | R raster rendering or mixed-language composition |
| `references/matplotlib.md` | Python implementation details |
| `references/complexheatmap.md` | ComplexHeatmap implementation |
| `references/checklist.md` | Before delivery |
| `references/revision-cases.md` | Reviewer simulation or a matching failure pattern |

## Deterministic tools

Run commands from the repository root:

```bash
# Skill and reference integrity
python scripts/check_references.py

# Trigger boundary benchmark
python scripts/trigger_benchmark.py

# QA rule coverage
python scripts/qa_coverage.py

# Audit one generated script
python scripts/qa_validator.py path/to/figure.py

# Rebuild README previews and atlases
python scripts/generate_readme_previews.py
python scripts/generate_palette_previews.py
python scripts/generate_atlas.py
```

## Production assets and adapters

- `assets/figures/<type>/`: reusable production scripts and companion previews.
- `assets/figure-atlas/`: README chart-index thumbnails.
- `assets/palette-gallery/`: named-theme RGB previews.
- `install/`: generated cross-platform adapters.
- `agents/openai.yaml`: Codex UI metadata.

Regenerate adapters after changing baseline rules:

```bash
python scripts/generate_adapters.py
```
