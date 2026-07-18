# Publication Figure QA Protocol

Execute this protocol after code generation and again after every visual revision. A figure is deliverable only when the rendered proof has been inspected at its intended display size.

## Contents

1. [Pass 0 — Anti-pattern scan](#pass-0--anti-pattern-scan)
2. [Pass 1 — Code and export compliance](#pass-1--code-and-export-compliance)
3. [Pass 2 — Scientific and visual logic](#pass-2--scientific-and-visual-logic)
4. [Pass 3 — Rendered proof inspection](#pass-3--rendered-proof-inspection)
5. [QA report](#qa-report)

## Automated checks

Run:

```bash
python scripts/qa_validator.py path/to/figure.py
```

The validator covers deterministic `AP` and `CL` checks. Passes 2 and 3 still require reasoning and visual inspection.

## Pass 0 — Anti-pattern scan

| ID | Check | Pass condition | Repair |
|---|---|---|---|
| `AP-0` | Baseline loaded | Typography, semantic colours, and export rules are explicit | Load the relevant reference blocks before plotting |
| `AP-1` | No default categorical palette | No `tab10`, seaborn default palette, ggplot hue scale, or unreviewed Brewer set | Use a named theme or user-confirmed hex colours |
| `AP-2` | No rainbow / jet | Continuous scales are perceptually ordered | Use a sequential or meaningful diverging map |
| `AP-3` | No decorative frame | Top/right spines and non-informative borders are removed | Keep only necessary axes |
| `AP-4` | No legend occlusion | Legend is outside the data region, in reserved whitespace, or replaced by direct labels | Move, reduce, or replace the legend |
| `AP-5` | Vector output included | Line art has PDF/SVG/EPS output | Add a vector export |
| `AP-6` | Small samples remain visible | For small groups, individual observations are shown | Overlay strip/swarm/scatter points |
| `AP-7` | Font is explicit | A journal-safe Latin/CJK font stack is configured | Load the typography baseline |

If Pass 0 finds more than two failures, repair them before continuing.

## Pass 1 — Code and export compliance

| ID | Check | Pass condition | Repair |
|---|---|---|---|
| `CL-1` | Final-size typography | Routine text is readable at final size; no text is below the documented floor | Increase type or simplify labels |
| `CL-2` | Physical dimensions | Width matches the target column, normally 89 mm or 183 mm; height does not exceed 247 mm | Set the canvas before plotting |
| `CL-3` | Raster resolution | Genuine raster proof is at least 450 dpi unless the target specification explicitly differs | Re-export at the required physical size and dpi |
| `CL-4` | Font embedding / editability | PDF text is embedded and SVG text remains editable where required | Use TrueType/Cairo-compatible export settings |
| `CL-5` | Line hierarchy | Axes are thinner than data marks; routine axes are approximately 0.5–0.8 pt | Reduce decorative or dominant strokes |
| `CL-6` | Tick treatment | Ticks are outward and do not collide with data | Set explicit tick direction and spacing |
| `CL-7` | Complete deliverables | Vector master plus RGB raster proof are produced; rasterized composite panels are disclosed | Export missing files and document limitations |

## Pass 2 — Scientific and visual logic

### `VI-1` Core conclusion visibility

Identify the element with the greatest visual weight. It must carry the figure's declared conclusion. If a secondary element dominates, revise size, position, contrast, or panel hierarchy.

### `VI-2` Colour accessibility

Critical comparisons must not depend on red–green hue or colour alone. Use direct labels, shape, line style, hatch, position, or ordering as redundant encoding.

### `VI-3` Data-ink discipline

Remove non-informative gradients, shadows, borders, duplicated legends, and dense grids. Keep a visual element only when it helps decode evidence.

### `VI-4` Axis integrity

- Bars start from zero unless an explicit axis break is justified and visible.
- Non-bar axes cover the relevant data range without exaggerating differences.
- Log scales are valid for the data and named in the axis label.
- Units and transformations are stated.

### `VI-5` Statistical completeness

When statistical claims appear, record:

- definition of `n`;
- centre statistic;
- SD, SEM, CI, IQR, or other interval;
- test name and multiple-comparison correction;
- exact p-values where practical;
- asterisk thresholds if asterisks are used.

### `VI-6` Multi-panel consistency

Panel letters, typography, semantic colours, axes, and annotation styles are consistent. Repeated labels may be removed only when a shared label preserves standalone interpretation.

### `VI-7` Known-reviewer-risk check

Read `revision-cases.md` when the chart type or journal matches a recorded failure pattern. Confirm that the current figure does not repeat that failure.

## Pass 3 — Rendered proof inspection

Render the final-size RGB PNG and inspect it visually. Code review alone cannot pass this stage.

### `VV-1` Occlusion

Check legends, point labels, significance brackets, colour bars, error bars, and panel letters. Nothing may cover data or another required label.

### `VV-2` Layout regularity

Check panel edges, gutters, margins, hero/support proportions, colour-bar alignment, and unintended empty space. Every asymmetry must have a scientific reason.

### `VV-3` Text legibility

Read every title, axis, tick, legend, gene name, and annotation at intended size. Fix clipping, missing glyphs, isolated one-character line wraps, and excessive rotation.

### `VV-4` Colour rendering

Check that adjacent categories remain distinct, ordered ramps progress visibly, light marks do not disappear on white, and neutral context does not overpower evidence.

### `VV-5` Data signal integrity

Confirm that every panel contains the evidence its chart type requires:

| Chart | Minimum sanity check |
|---|---|
| Volcano | Non-significant and significant points both exist; thresholds are stated |
| ROC | Curves are above chance without implausible immediate saturation |
| Heatmap | Values and row/column variation are non-degenerate |
| Bar / dot | Group summaries differ only when supported by observations |
| Correlation | Off-diagonal structure and sample size support the interpretation |
| PCA / RDA | Separation claims match the plotted overlap and explained variance |
| Box / violin | Observations and group distributions are visible |
| Scatter | A fitted relation is shown only when justified by the data |
| Trend | x is ordered and uncertainty is represented when available |

For simulated examples, also check that no panel is blank or saturated. For real data, a weak signal is valid and must not be cosmetically strengthened.

### `VV-6` Grayscale proof and redundant encoding

Generate:

```bash
python scripts/grayscale_proof.py figure-proof.png --output figure-proof-grayscale.png
```

Inspect RGB and grayscale proofs side by side. Critical groups, thresholds, and highlighted observations must remain identifiable through luminance or non-colour encoding. If they merge, add direct labels, markers, line styles, hatches, or unambiguous ordering before adjusting hue.

## Render-fix loop

1. Run the programmatic layout gate.
2. Inspect `VV-1` through `VV-6` in order.
3. Repair every failure.
4. Re-render and re-inspect the affected checks.
5. After three unsuccessful cycles, restructure the layout or enter reviewer-simulation mode.

If no Python/R runtime is available, report that Pass 3 was not executed; do not call the figure publication-ready.

## QA report

```text
Figure:
Target journal and column:
Backend:
Theme:

Pass 0 — AP-0..AP-7:
Pass 1 — CL-1..CL-7:
Pass 2 — VI-1..VI-7:
Pass 3 — VV-1..VV-6:

RGB proof:
Grayscale proof:
Editable vector masters:
Rasterized panels in composite:
Warnings:

Verdict: READY / FIX / BLOCKED
```

- `READY`: all required passes completed with no unresolved failure.
- `FIX`: repairable failures remain; revise and re-run.
- `BLOCKED`: runtime, data, font, or export limitations prevent a complete review.
