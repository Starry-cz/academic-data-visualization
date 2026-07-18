<p align="center">
  <img src="assets/readme/academic-data-visualization-workflow-v5.png" width="100%" alt="Academic Data Visualization: complete workflow and figure atlas from research question to publication-ready delivery">
</p>

<div align="center">

# Academic Data Visualization

**A publication-grade scientific-visualization skill: from research question to reproducible, reviewable figures.**

It helps AI coding assistants understand what the evidence must show, choose figure types, build a multi-panel story, apply a coherent visual system, and deliver editable submission assets.

[![Stars](https://img.shields.io/github/stars/Starry-cz/academic-data-visualization?style=flat-square&color=E69F00&label=stars)](https://github.com/Starry-cz/academic-data-visualization/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/Starry-cz/academic-data-visualization?style=flat-square&color=0072B2)](https://github.com/Starry-cz/academic-data-visualization/commits/main)
[![License](https://img.shields.io/github/license/Starry-cz/academic-data-visualization?style=flat-square&color=009E73)](LICENSE)

[Quick start](#quick-start) · [Say this directly](#say-this-directly) · [All charts](#all-chart-navigation) · [Install & update](#installation-and-updates) · [Quality assurance](#quality-assurance) · [中文](README.md)

</div>

<p align="center">
  <strong>Research question · data structure · figure selection · panel narrative · QA · submission-ready delivery</strong>
</p>

> The figures demonstrate visual language and information hierarchy only. Every production figure is rebuilt around the user's real data, research question, and target journal.

## Quick start

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git
```

Place the **entire directory** in your agent's skills folder; do not copy `SKILL.md` alone. The `references/`, `scripts/`, and `assets/` directories provide the figure rules, QA, and reusable production assets together.

Then describe the task naturally. Rather than forcing data into a template, the skill first confirms the research question, data structure, and target journal before proposing a figure plan.

## Say this directly

After installation, give the agent your data, an existing figure, or a research goal. Copy and adapt any of these prompts.

| Situation | Prompt |
|---|---|
| Unsure which figure to use | `Use academic-data-visualization to analyse experiment.csv. Compare three interventions across four time points, foreground group differences and uncertainty, and target a double-column journal figure. Propose and justify the figure plan before generating it.` |
| Build a multi-panel main figure | `Use academic-data-visualization to organize these results into a submission-ready main figure. State what each panel answers and how the hero and supporting panels form one evidence story.` |
| Rebuild or improve an old figure | `Use academic-data-visualization with old_figure.png and source_data.csv to rebuild an editable, muted, publication-grade figure. Preserve the data meaning; do not merely beautify the screenshot.` |
| Adapt to a target journal | `Use academic-data-visualization to review and rebuild figure.py for a Nature double-column figure, including size, type, and export requirements.` |
| Audit before submission | `Use academic-data-visualization to audit this figure script for statistical expression, colour-blind readability, text clipping, panel alignment, and vector-export risks.` |

If you provide data without a scientific question, the skill asks what you need to learn before generating a generic set of plots.

## Capabilities and figure types

| Task | What the skill does | Outcome |
|---|---|---|
| Choosing a figure | Reasons from the question, variable types, sample size, distribution, and grouping | A justified single-figure or multi-panel proposal |
| Improving default-looking figures | Applies typography, semantic colour, spacing, line weight, and annotation hierarchy | Publication-ready visual consistency |
| Combining evidence | Identifies a hero panel, arranges supporting panels, and preserves colour semantics | A readable multi-panel narrative |
| Reproducing old figures | Reuses relevant production scripts and inherits dimensional and proportional parameters | Traceable, iterative code |
| Reviewing before submission | Audits figure choice, statistical expression, export, readability, and accessibility risks | An actionable revision checklist |

Coverage includes correlation matrices, heatmaps, scatter / PCA / RDA, bars and uncertainty, box / violin / ridge plots, trends, volcanoes, AUROC, forest plots, Mantel, Sankey, UpSet, confusion matrices, and long-tail scientific figure types. The full research-and-work chart-selection guide is in [`references/figure-type-catalog.md`](references/figure-type-catalog.md); it organizes comparison, distribution, time, relationship, omics, model, spatial, network, and operational charts while distinguishing existing templates from on-demand implementations.

## Nature-ready figure standard

The skill does not imitate the decoration of one Nature paper. It translates Nature's official figure requirements into executable defaults.

| Dimension | Default |
|---|---|
| Typography | Arial / Helvetica; 5–7 pt routine text at final size; 8 pt bold upright lowercase panel labels |
| Colour | Colourblind-safe semantic colours; concepts stay consistent across panels; colour is never the only identifier |
| Axes and whitespace | Keep necessary axes, ticks, and units; omit background grids, shadows, and decorative icons by default |
| Delivery | RGB; editable PDF / SVG for text and line art; 450 dpi PNG / TIFF for genuinely raster content |

See [`references/nature-publication-style.md`](references/nature-publication-style.md) for the complete contract, linked to [`references/typography.md`](references/typography.md), [`references/color-palettes.md`](references/color-palettes.md), and [`references/export-specs.md`](references/export-specs.md).

## All chart navigation

The skill currently includes **96 reusable chart visual patterns**. Put any name below directly in a prompt; if the choice is unclear, describe the research question and the skill will recommend a data-appropriate option.

<table>
  <thead>
    <tr>
      <th width="22%">Chart family</th>
      <th width="68%">Available chart types</th>
      <th width="10%">Atlas</th>
    </tr>
  </thead>
  <tbody>
    <tr><td valign="top"><strong>Comparison, ranking, and composition</strong></td><td valign="top">Grouped bar, stacked bar, horizontal bar, bars with raw points, significance bars, paired bars, dot plot, bar + strip overlay, 100% stacked bar, diverging bar, waterfall, lollipop, horizontal percent stacked bar, nested grouped bar, error bars, range plot</td><td valign="top"><a href="assets/chart-atlas/atlas-01-bar-charts.png">Bar and comparison atlas</a></td></tr>
    <tr><td valign="top"><strong>Trends, scatter, and relationships</strong></td><td valign="top">Scatter, regression scatter, multi-series line, dose-response scatter, correlation scatter, bubble, mean ± SEM ribbon, scatter with marginal histogram, step chart, connected scatter, multi-group scatter, LOESS, stem plot, polar scatter, area chart, highlighted trend</td><td valign="top"><a href="assets/chart-atlas/atlas-02-line-scatter.png">Trend and relationship atlas</a></td></tr>
    <tr><td valign="top"><strong>Heatmaps, matrices, and patterns</strong></td><td valign="top">Diverging heatmap, masked correlation matrix, annotated heatmap, split heatmap, clustered heatmap, density heatmap, categorical heatmap, half-dendrogram heatmap, upper-triangle correlation matrix, row-normalized heatmap, discrete heatmap, sparse-matrix heatmap, multi-annotation heatmap, gapped heatmap, binary heatmap, continuous-gradient heatmap</td><td valign="top"><a href="assets/chart-atlas/atlas-03-heatmaps.png">Heatmap and matrix atlas</a></td></tr>
    <tr><td valign="top"><strong>Distributions and statistical diagnostics</strong></td><td valign="top">Box plot, violin plot, box + raw points, histogram, overlapping KDE, ridge plot, half violin, beeswarm, Sina plot, split violin, ECDF, QQ plot, overlapping histogram, raincloud, 2D histogram, rug plot</td><td valign="top"><a href="assets/chart-atlas/atlas-04-distributions.png">Distribution atlas</a></td></tr>
    <tr><td valign="top"><strong>Research, models, and omics</strong></td><td valign="top">Standard volcano, labelled volcano, faceted volcano, MA plot, quadrant scatter, forest plot, radar chart, UpSet, genomic waterfall, Manhattan plot, Bland–Altman plot, ROC curve, PR curve, calibration curve, meta-analysis funnel plot, Venn diagram</td><td valign="top"><a href="assets/chart-atlas/atlas-05-volcano-special.png">Research and model atlas</a></td></tr>
    <tr><td valign="top"><strong>Domain research and everyday work</strong></td><td valign="top">Kaplan–Meier survival, dumbbell, slopegraph, Pareto, control chart, Gantt, stage funnel, treemap, calendar heatmap, network, spatial bubble, dendrogram, genomic lollipop, SHAP beeswarm, coefficient / dot-whisker, ternary plot</td><td valign="top"><a href="assets/chart-atlas/atlas-06-domain-work.png">Domain and work atlas</a></td></tr>
  </tbody>
</table>

> The atlases show reusable visual patterns. For production templates, on-demand types, and data constraints, see [`references/figure-type-catalog.md`](references/figure-type-catalog.md) and [`references/directory-map.md`](references/directory-map.md).

## Figure catalog

<table>
  <thead><tr><th width="17%">Figure name</th><th width="25%">Preview</th><th width="28%">Graphical characteristics</th><th width="30%">Typical use cases</th></tr></thead>
  <tbody>
    <tr><td valign="top">3D heatmap</td><td align="center" valign="top"><img src="assets/figure-atlas/3Dheatmap.png" width="190"></td><td valign="top">A three-dimensional column surface encodes matrix values through height and colour</td><td valign="top">Multifactor interactions, genotype × environment matrices, and 3D intensity distributions</td></tr>
    <tr><td valign="top">AUROC curve</td><td align="center" valign="top"><img src="assets/figure-atlas/auroc.png" width="190"></td><td valign="top">TPR–FPR curves with a diagonal reference and AUC annotation</td><td valign="top">Classifier evaluation, multi-model ROC comparison, and threshold sensitivity</td></tr>
    <tr><td valign="top">Bar chart</td><td align="center" valign="top"><img src="assets/figure-atlas/bar.png" width="190"></td><td valign="top">Bar height encodes a univariate summary; supports uncertainty and raw samples</td><td valign="top">Group means, single-metric ranking, and count summaries</td></tr>
    <tr><td valign="top">Correlation-density plot</td><td align="center" valign="top"><img src="assets/figure-atlas/CorrelationDensity.png" width="190"></td><td valign="top">Scatter overlaid with 2D kernel-density contours and a fitted relationship</td><td valign="top">Bivariate association, dense-region identification, and outlier detection</td></tr>
    <tr><td valign="top">Correlation matrix</td><td align="center" valign="top"><img src="assets/figure-atlas/Correlationmatrix.png" width="190"></td><td valign="top">Square grid with colour and values for pairwise correlation coefficients</td><td valign="top">Multivariable correlation overview and pre-selection collinearity checks</td></tr>
    <tr><td valign="top">Density heatmap</td><td align="center" valign="top"><img src="assets/figure-atlas/density_heatmap.png" width="190"></td><td valign="top">Continuous 2D kernel density fills a grid with a colour gradient</td><td valign="top">Large point-cloud density distributions and alternatives to overplotted scatter</td></tr>
    <tr><td valign="top">Frequency 3D heatmap</td><td align="center" valign="top"><img src="assets/figure-atlas/Frequency_3DHeatmap.png" width="190"></td><td valign="top">Three-dimensional columns display binned frequency while retaining group structure</td><td valign="top">Allele-frequency distributions and two-factor count cross-tabulations</td></tr>
    <tr><td valign="top">Grouped correlation matrix</td><td align="center" valign="top"><img src="assets/figure-atlas/GroupCorrelationmatrix.png" width="190"></td><td valign="top">Multiple correlation matrices are split and arranged by group</td><td valign="top">Comparing correlation structures across treatments or environments</td></tr>
    <tr><td valign="top">Grouped bar chart</td><td align="center" valign="top"><img src="assets/figure-atlas/GroupedBarChart.png" width="190"></td><td valign="top">Parallel subgroup bars within a category, with optional uncertainty</td><td valign="top">Multi-treatment × multi-metric comparisons and repeated-experiment differences</td></tr>
    <tr><td valign="top">Mantel correlation test</td><td align="center" valign="top"><img src="assets/figure-atlas/MantelCorrelation.png" width="190"></td><td valign="top">A correlation-matrix heatmap overlaid with links, Mantel r, and significance</td><td valign="top">Links between environmental and community / genotype matrices; distance-matrix analysis</td></tr>
    <tr><td valign="top">PCA biplot</td><td align="center" valign="top"><img src="assets/figure-atlas/PCA.png" width="190"></td><td valign="top">Principal-component scatter, group ellipses, and variable loadings combined</td><td valign="top">Sample separation, population structure, dimension reduction, and variable contributions</td></tr>
    <tr><td valign="top">Radar chart</td><td align="center" valign="top"><img src="assets/figure-atlas/radar.png" width="190"></td><td valign="top">A closed multi-axis profile compares relative performance across indicators</td><td valign="top">Multi-indicator profiles for a small number of objects or treatments</td></tr>
    <tr><td valign="top">Ridge plot</td><td align="center" valign="top"><img src="assets/figure-atlas/RidgePlot.png" width="190"></td><td valign="top">Offset kernel-density curves stack distributions vertically</td><td valign="top">Distribution shifts and overlap across groups or time points</td></tr>
    <tr><td valign="top">Sankey diagram</td><td align="center" valign="top"><img src="assets/figure-atlas/sankey.png" width="190"></td><td valign="top">Band width encodes flow between sources, processes, and destinations</td><td valign="top">Category flows, material / energy transfer, and state transitions</td></tr>
    <tr><td valign="top">Stacked-bar scatter plot</td><td align="center" valign="top"><img src="assets/figure-atlas/StackedBarScatter.png" width="190"></td><td valign="top">Stacked composition and raw scatter are combined to show proportions and individual variation</td><td valign="top">Composition comparisons alongside sample-level observations</td></tr>
    <tr><td valign="top">Trend plot</td><td align="center" valign="top"><img src="assets/figure-atlas/trend.png" width="190"></td><td valign="top">Continuous lines show directional change over time, dose, or gradient</td><td valign="top">Time series, dose response, and environmental-gradient trends</td></tr>
    <tr><td valign="top">Violin plot</td><td align="center" valign="top"><img src="assets/figure-atlas/violin_chart.png" width="190"></td><td valign="top">Density silhouettes combine with median, quartile, or other statistical summaries</td><td valign="top">Group distribution, spread, and outlier comparison</td></tr>
  </tbody>
</table>

### Research and work extension atlas

Beyond the production types above, the skill now includes 16 reusable visual patterns for research and everyday work: Kaplan–Meier, survival / effect estimates, dumbbell, slopegraph, Pareto, control chart, Gantt, stage funnel, treemap, calendar heatmap, network, spatial bubble, dendrogram, genomic lollipop, SHAP beeswarm, and ternary plots. See [`references/figure-type-catalog.md`](references/figure-type-catalog.md) for selection rules and constraints.

<p align="center">
  <img src="assets/chart-atlas/atlas-06-domain-work.png" width="100%" alt="Research and work extension atlas: Kaplan-Meier, Gantt, network, SHAP beeswarm, and more">
</p>

## Workflow and visual system

```text
Research question → data structure → figure justification → panel design → style injection
                                          → script / asset matching → native render → QA → submission-ready delivery
```

1. Establish the research question, target journal, and core conclusion.
2. Inspect variable types, groups, sample size, distributions, and outliers; then propose a figure plan.
3. Organize a hero panel and supporting panels around one conclusion rather than a fixed template.
4. Apply typography, physical dimensions, semantic colour, statistical annotation, and export rules; reuse production scripts where suitable.
5. Deliver PNG previews, SVG/PDF masters, submission-grade TIFF, and both code and visual QA.

The default visual language uses a Nature-ready, colourblind-safe semantic system rather than matplotlib or ggplot defaults: blue `#0072B2`, bluish green `#009E73`, orange `#E69F00`, purple `#CC79A7`, vermilion `#D55E00`, and ink grey `#1A1A1A`. See [`references/color-palettes.md`](references/color-palettes.md) and [`references/visual-style.md`](references/visual-style.md) for implementation rules.

## Installation and updates

### Codex

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git
mkdir -p ~/.codex/skills/academic-data-visualization
cp -r academic-data-visualization/* ~/.codex/skills/academic-data-visualization/
```

When you retain the local clone, update it later with:

```bash
git pull
```

### Claude Code, Cursor, and GitHub Copilot

- **Claude Code:** copy the full directory to `~/.claude/skills/academic-data-visualization/`.
- **Cursor:** copy [`install/cursor/.cursorrules`](install/cursor/.cursorrules) to the target project root.
- **GitHub Copilot:** copy [`install/copilot/copilot-instructions.md`](install/copilot/copilot-instructions.md) to the target project's `.github/` directory.

Platform adapters live in [`install/`](install/); the Codex entry instructions are in [`install/codex/instructions.md`](install/codex/instructions.md).

## Quality assurance

Quality checks cover scientific-communication risks beyond whether a script runs:

- **anti-patterns:** default/rainbow palettes, heavy borders, occluding legends, and low-resolution screenshots;
- **code and export:** fonts, column width, line weight, semantic colours, editable vector text, and resolution;
- **data and evidence:** inappropriate summary bars, missing samples, correlation / separation claims, and statistical annotations;
- **visual review:** clipping, overlapping ticks, panel alignment, greyscale and colour-blind readability.

```bash
# Check one figure-generation script
python scripts/qa_validator.py path/to/figure.py

# Run QA coverage tests and rebuild README previews
python scripts/qa_coverage.py
python scripts/generate_readme_previews.py
python scripts/generate_atlas.py
```

## Repository layout

```text
academic-data-visualization/
├── SKILL.md                 # Agent entry point and complete workflow
├── references/              # figure, visual, export, and QA rules
├── scripts/                 # composition, validation, preview, and atlas generators
├── assets/                  # reusable production scripts and README previews
└── install/                 # Codex / Cursor / Copilot / Claude adapters
```

## Contributing and license

Issues and pull requests are welcome, especially for journal specifications, accessibility improvements, figure types, and real research scenarios. New templates should include a reproducible script, data assumptions, and a rendered preview.

Licensed under [Apache-2.0](LICENSE).
