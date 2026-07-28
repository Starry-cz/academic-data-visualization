<p align="center">
  <img src="assets/readme/academic-data-visualization-workflow-v5.png" width="100%" alt="Workflow from research question and data profiling to publication-ready figures and visual review">
</p>

<h1 align="center">Academic Data Visualization</h1>

<p align="center">
  <strong>Research question → data contract → chart rationale → publication-ready figure</strong><br>
  <sub>Turn real data and journal constraints into reproducible, reviewable Python / R scientific figures.</sub>
</p>

<p align="center">
  <a href="references/figure-type-catalog.md"><img src="https://img.shields.io/badge/Taxonomy-24_categories-4573B4?style=flat-square" alt="24-category chart taxonomy"></a>
  <a href="#capability-scope"><img src="https://img.shields.io/badge/Source_memberships-714%2F714-73C79E?style=flat-square" alt="714/714 source memberships mapped"></a>
  <a href="references/directory-map.md"><img src="https://img.shields.io/badge/Production_assets-34_verified-F2A65A?style=flat-square" alt="34 verified production assets"></a>
  <a href="#quality-evidence"><img src="https://img.shields.io/badge/QA-4_passes-95AEDA?style=flat-square" alt="Four-pass QA"></a>
  <a href="https://github.com/Starry-cz/academic-data-visualization/actions/workflows/quality.yml"><img src="https://github.com/Starry-cz/academic-data-visualization/actions/workflows/quality.yml/badge.svg" alt="Automated quality checks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0-7A939F?style=flat-square" alt="Apache-2.0 License"></a>
</p>

<p align="center">
  <a href="#30-second-start">Quick start</a> ·
  <a href="#why-use-it">Why</a> ·
  <a href="#capability-scope">Scope</a> ·
  <a href="#selected-figures">Gallery</a> ·
  <a href="#documentation-map">Docs</a> ·
  <a href="#quality-evidence">Quality</a> ·
  <a href="README.md">中文</a>
</p>

> This is not a gallery that forces data into preset templates. It first defines the claim, unit of observation, variable structure, and submission target; then it selects a chart, reuses a verified asset or implements one on demand, and reviews final-size RGB and grayscale proofs through four QA passes.

## 30-second start

Install the complete Skill rather than copying `SKILL.md` alone:

```powershell
# Windows PowerShell · Codex
git clone https://github.com/Starry-cz/academic-data-visualization.git "$env:USERPROFILE\.codex\skills\academic-data-visualization"
```

```bash
# macOS / Linux · Codex
git clone https://github.com/Starry-cz/academic-data-visualization.git ~/.codex/skills/academic-data-visualization
```

Then describe the research question, data, and deliverables:

```text
Use academic-data-visualization to analyse experiment.csv.
I need to compare three treatments at four time points. Profile sample sizes, distributions,
missingness, and repeated-measures structure before defending the chart and multipanel design.
Target a two-column manuscript figure and deliver an editable vector master, a 450 dpi proof,
a grayscale proof, and a QA report.
```

## Why use it

<table width="100%" align="center">
  <tr>
    <th width="25%">Claim first</th>
    <th width="25%">Honest boundaries</th>
    <th width="25%">Reusable assets</th>
    <th width="25%">Submission-ready QA</th>
  </tr>
  <tr>
    <td width="25%">Decide what readers must compare, relate, or judge before choosing a chart</td>
    <td width="25%">All 665 canonical records expose their real implementation state</td>
    <td width="25%">34 asset families include scripts, previews, and manifests</td>
    <td width="25%">Review anti-patterns, code and export, scientific logic, and final rendering</td>
  </tr>
</table>

Conventional plotting requests start with “make a bar chart” or “draw a heatmap.” This Skill starts with the scientific claim and data contract, and actively blocks common risks such as small-sample mean bars, dual axes, rainbow maps, invalid connecting lines, and misleading truncation.

## How it works

<table width="100%" align="center">
  <tr><th width="20%">Stage</th><th width="60%">Key action</th><th width="20%">Output</th></tr>
  <tr><td width="20%"><strong>1. Define</strong></td><td width="60%">Fix the claim, observation unit, variables, dependence, and target journal</td><td width="20%"><a href="references/figure-contract.md">Figure contract</a></td></tr>
  <tr><td width="20%"><strong>2. Defend</strong></td><td width="60%">Profile sample sizes, distributions, missingness, outliers, and groups; compare candidates</td><td width="20%">Rationale and risks</td></tr>
  <tr><td width="20%"><strong>3. Implement</strong></td><td width="60%">Route to a production template, reusable pattern, or on-demand build; unify panels and colour</td><td width="20%">Python / R and vector master</td></tr>
  <tr><td width="20%"><strong>4. Verify</strong></td><td width="60%">Run programmatic checks and inspect final-size RGB, grayscale, and export proofs</td><td width="20%">Proofs and QA report</td></tr>
</table>

## Capability scope

<!-- chart-registry:summary:start -->
The registry separates catalogue coverage from implementation status. Only production templates have reusable scripts, previews, and manifests.

<table width="100%" align="center">
  <tr><td width="50%"><strong>Taxonomy categories</strong></td><td width="50%">24</td></tr>
  <tr><td width="50%"><strong>Canonical chart records</strong></td><td width="50%">665</td></tr>
  <tr><td width="50%"><strong>Source taxonomy records</strong></td><td width="50%">625</td></tr>
  <tr><td width="50%"><strong>Repository extensions</strong></td><td width="50%">40</td></tr>
  <tr><td width="50%"><strong>Source memberships</strong></td><td width="50%">714 / 714 mapped</td></tr>
  <tr><td width="50%"><strong>Production templates</strong></td><td width="50%">34</td></tr>
  <tr><td width="50%"><strong>Reusable patterns</strong></td><td width="50%">228</td></tr>
  <tr><td width="50%"><strong>On-demand routes</strong></td><td width="50%">403</td></tr>
</table>
<!-- chart-registry:summary:end -->

<table width="100%" align="center">
  <tr><th width="25%">State</th><th width="25%">Meaning</th><th width="50%">Repository promise</th></tr>
  <tr><td width="25%"><code>production_template</code></td><td width="25%">Verified template</td><td width="50%">Real script + PNG + <code>asset.yaml</code>, with SVG/PDF where available</td></tr>
  <tr><td width="25%"><code>reusable_pattern</code></td><td width="25%">Reusable pattern</td><td width="50%">Explicit data contract and backend route, but no claim of a standalone asset</td></tr>
  <tr><td width="25%"><code>on_demand</code></td><td width="25%">Built for actual data</td><td width="50%">No fake previews and no look-alike substitutes for specialist charts</td></tr>
</table>

Browse the [complete 24-category catalogue](references/figure-type-catalog.md), [bilingual alias index](references/chart-alias-index.md), [coverage audit](references/chart-coverage-audit.md), and [verified production-asset map](references/directory-map.md).

## Selected figures

The landing page shows 22 verified examples across distinct chart families. Every thumbnail uses a fixed canvas so paired cells remain aligned; click an image for the original figure. Use the [production asset directory](assets/figures/) and [chart catalogue](references/figure-type-catalog.md) for complete implementation states.

### Relationships, ordination, diagnostics, and high-dimensional structure · 3 × 4

<table width="100%" align="center">
  <tr>
    <td width="33%" align="center" valign="top"><strong>3D heatmap</strong><br><a href="assets/figure-atlas/3Dheatmap.png"><img src="assets/figure-atlas/readme-cards/3Dheatmap.png" width="280" alt="3D heatmap"></a><br><sub>High-dimensional intensity</sub></td>
    <td width="34%" align="center" valign="top"><strong>Density heatmap</strong><br><a href="assets/figure-atlas/density_heatmap.png"><img src="assets/figure-atlas/readme-cards/density_heatmap.png" width="280" alt="Density heatmap"></a><br><sub>2D density and clusters</sub></td>
    <td width="33%" align="center" valign="top"><strong>PCA biplot</strong><br><a href="assets/figure-atlas/PCA.png"><img src="assets/figure-atlas/readme-cards/PCA.png" width="280" alt="PCA biplot"></a><br><sub>Sample separation and loadings</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><strong>AUROC</strong><br><a href="assets/figure-atlas/auroc.png"><img src="assets/figure-atlas/readme-cards/auroc.png" width="280" alt="AUROC curve"></a><br><sub>Model discrimination</sub></td>
    <td width="34%" align="center" valign="top"><strong>Correlation density</strong><br><a href="assets/figure-atlas/CorrelationDensity.png"><img src="assets/figure-atlas/readme-cards/CorrelationDensity.png" width="280" alt="Correlation density plot"></a><br><sub>Relationships and local density</sub></td>
    <td width="33%" align="center" valign="top"><strong>Correlation matrix</strong><br><a href="assets/figure-atlas/Correlationmatrix.png"><img src="assets/figure-atlas/readme-cards/Correlationmatrix.png" width="280" alt="Correlation matrix"></a><br><sub>Multivariable relationships</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><strong>Grouped correlation</strong><br><a href="assets/figure-atlas/GroupCorrelationmatrix.png"><img src="assets/figure-atlas/readme-cards/GroupCorrelationmatrix.png" width="280" alt="Grouped correlation matrix"></a><br><sub>Condition-specific structure</sub></td>
    <td width="34%" align="center" valign="top"><strong>Radar plot</strong><br><a href="assets/figure-atlas/radar.png"><img src="assets/figure-atlas/readme-cards/radar.png" width="280" alt="Radar plot"></a><br><sub>Few objects, many metrics</sub></td>
    <td width="33%" align="center" valign="top"><strong>Ridge plot</strong><br><a href="assets/figure-atlas/RidgePlot.png"><img src="assets/figure-atlas/readme-cards/RidgePlot.png" width="280" alt="Ridge plot"></a><br><sub>Distribution shifts</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><strong>Bubble scatter</strong><br><a href="assets/figures/BubbleScatter/bubble_scatter.png"><img src="assets/figure-atlas/readme-cards/bubble_scatter.png" width="280" alt="Bubble scatter plot"></a><br><sub>2D relationship plus size</sub></td>
    <td width="34%" align="center" valign="top"><strong>Correlation bubbles</strong><br><a href="assets/figures/CorrelationBubbleMatrix/correlation_bubble_matrix.png"><img src="assets/figure-atlas/readme-cards/correlation_bubble_matrix.png" width="280" alt="Correlation bubble matrix"></a><br><sub>Direction, strength, significance</sub></td>
    <td width="33%" align="center" valign="top"><strong>Correlation network</strong><br><a href="assets/figures/CorrelationNetwork/correlation_network.png"><img src="assets/figure-atlas/readme-cards/correlation_network.png" width="280" alt="Correlation network"></a><br><sub>Edges and community structure</sub></td>
  </tr>
</table>

### Comparison, distribution, trend, composition, and space · 2 × 5

<table width="100%" align="center">
  <tr>
    <td width="50%" align="center" valign="top"><strong>Bar plot</strong><br><a href="assets/figure-atlas/bar.png"><img src="assets/figure-atlas/readme-cards/bar.png" width="390" alt="Bar plot"></a><br><sub>Group summaries and observations</sub></td>
    <td width="50%" align="center" valign="top"><strong>Grouped bars</strong><br><a href="assets/figure-atlas/GroupedBarChart.png"><img src="assets/figure-atlas/readme-cards/GroupedBarChart.png" width="390" alt="Grouped bar chart"></a><br><sub>Multiple treatments × metrics</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Mantel correlation</strong><br><a href="assets/figure-atlas/MantelCorrelation.png"><img src="assets/figure-atlas/readme-cards/MantelCorrelation.png" width="390" alt="Mantel correlation"></a><br><sub>Distance matrices and environment</sub></td>
    <td width="50%" align="center" valign="top"><strong>Violin plot</strong><br><a href="assets/figure-atlas/violin_chart.png"><img src="assets/figure-atlas/readme-cards/violin_chart.png" width="390" alt="Violin plot"></a><br><sub>Distribution shape and outliers</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Time trend</strong><br><a href="assets/figure-atlas/trend.png"><img src="assets/figure-atlas/readme-cards/trend.png" width="390" alt="Time trend"></a><br><sub>Trajectories and uncertainty</sub></td>
    <td width="50%" align="center" valign="top"><strong>Stacked bar + scatter</strong><br><a href="assets/figure-atlas/StackedBarScatter.png"><img src="assets/figure-atlas/readme-cards/StackedBarScatter.png" width="390" alt="Stacked bar and scatter plot"></a><br><sub>Composition and observations</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Frequency 3D heatmap</strong><br><a href="assets/figure-atlas/Frequency_3DHeatmap.png"><img src="assets/figure-atlas/readme-cards/Frequency_3DHeatmap.png" width="390" alt="Frequency 3D heatmap"></a><br><sub>Two-factor binned frequency</sub></td>
    <td width="50%" align="center" valign="top"><strong>Sankey diagram</strong><br><a href="assets/figure-atlas/sankey.png"><img src="assets/figure-atlas/readme-cards/sankey.png" width="390" alt="Sankey diagram"></a><br><sub>Category flows and transitions</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Stacked area</strong><br><a href="assets/figures/StackedArea/stacked_area.png"><img src="assets/figure-atlas/readme-cards/stacked_area.png" width="390" alt="Stacked area chart"></a><br><sub>Composition over time</sub></td>
    <td width="50%" align="center" valign="top"><strong>Geographic bubble map</strong><br><a href="assets/figures/GeographicBubbleMap/geographic_bubble_map.png"><img src="assets/figure-atlas/readme-cards/geographic_bubble_map.png" width="390" alt="Geographic bubble map"></a><br><sub>Location and magnitude</sub></td>
  </tr>
</table>

## Colour system

Twenty-three themes cover categorical, sequential, and diverging semantics. The defaults require colour-blind safety, grayscale legibility, stable meaning, and a review step when colours are extracted from reference images.

<table width="100%" align="center">
  <tr>
    <td width="50%" align="center" valign="top"><strong>Nature default</strong><br><img src="assets/palette-gallery/nature-default.png" width="390" alt="Nature default palette preview"></td>
    <td width="50%" align="center" valign="top"><strong>Blue–red signal</strong><br><img src="assets/palette-gallery/blue-red-signal.png" width="390" alt="Blue-red signal palette preview"></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Pastel harmony</strong><br><img src="assets/palette-gallery/pastel-harmony.png" width="390" alt="Pastel harmony palette preview"></td>
    <td width="50%" align="center" valign="top"><strong>Coastal sunset</strong><br><img src="assets/palette-gallery/coastal-sunset.png" width="390" alt="Coastal sunset palette preview"></td>
  </tr>
</table>

See [`color-palettes.md`](references/color-palettes.md) and [`palette-library.json`](references/palette-library.json) for complete values, semantic roles, and usage constraints.

## Scope boundaries

<table width="100%" align="center">
  <tr><th width="50%">Good fit</th><th width="50%">Out of scope</th></tr>
  <tr><td width="50%">Manuscript main figures, supplements, theses, and scientific reports</td><td width="50%">Interactive dashboards or web data products</td></tr>
  <tr><td width="50%">Choosing a defensible chart from the real data structure</td><td width="50%">Illustration-only mechanisms with no quantitative panels</td></tr>
  <tr><td width="50%">Rebuilding old figures, unifying panels, or adapting to a journal</td><td width="50%">Statistical analysis, cleaning, or literature review with no figure goal</td></tr>
  <tr><td width="50%">Pre-submission checks for clipping, overlap, grayscale, encodings, and export</td><td width="50%">Pretending that a generic chart is a map, genome track, or 3D volume</td></tr>
</table>

## Documentation map

<table width="100%" align="center">
  <tr><th width="50%">Need</th><th width="50%">Start here</th></tr>
  <tr><td width="50%">Find a chart, alias, and real implementation state</td><td width="50%"><a href="references/figure-type-catalog.md">Chart catalogue</a> · <a href="references/chart-alias-index.md">Alias index</a> · <a href="references/chart-registry.yaml">Registry</a></td></tr>
  <tr><td width="50%">Define inputs, claims, and deliverables</td><td width="50%"><a href="references/figure-contract.md">Figure contract</a> · <a href="references/figure-design-brief.md">Design brief</a></td></tr>
  <tr><td width="50%">Organise multipanel hierarchy</td><td width="50%"><a href="references/multipanel-layout.md">Multipanel layout</a> · <a href="references/visual-style.md">Visual style</a></td></tr>
  <tr><td width="50%">Match journal dimensions and export</td><td width="50%"><a href="references/journal-intel.md">Journal intelligence</a> · <a href="references/journal-specs.md">Journal specs</a> · <a href="references/export-specs.md">Export specs</a></td></tr>
  <tr><td width="50%">Select or extend a palette</td><td width="50%"><a href="references/color-palettes.md">Colour guide</a> · <a href="references/palette-library.json">Palette registry</a></td></tr>
  <tr><td width="50%">Reuse assets and run final checks</td><td width="50%"><a href="references/asset-reuse-protocol.md">Asset reuse protocol</a> · <a href="references/checklist.md">Four-pass QA checklist</a></td></tr>
</table>

## More installation options

The complete repository matters: `references/`, `scripts/`, and `assets/` jointly provide routing, constraints, production assets, and QA. Do not copy a single file.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git ~/.claude/skills/academic-data-visualization
```

</details>

<details>
<summary><strong>Cursor</strong></summary>

Keep the complete Skill and use [`install/cursor/.cursorrules`](install/cursor/.cursorrules) where appropriate.

</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

Use [`install/copilot/copilot-instructions.md`](install/copilot/copilot-instructions.md) as repository instructions.

</details>

Update an existing installation with:

```bash
git -C ~/.codex/skills/academic-data-visualization pull
```

## Quality evidence

Current repository baseline:

- **714 / 714** source memberships are reproducibly mapped;
- **34 / 34** production asset families contain real scripts, PNGs, and manifests;
- **88 / 88** trigger-boundary cases classify correctly;
- **26 / 26** QA fixtures hit their expected results across **15 / 15** programmatic checks;
- CI audits the registry schema, 24 generated category documents, alias conflicts, asset mapping, and README summaries.

```bash
python scripts/check_skill_metadata.py
python scripts/check_references.py
python scripts/check_chart_registry.py
python scripts/build_chart_registry.py --check
python scripts/generate_chart_catalog.py --check
python -m unittest discover -s tests -v
python scripts/trigger_benchmark.py
python scripts/qa_coverage.py
python -m compileall -q scripts assets/figures tests
```

A result is marked `READY` only after all four passes in [`checklist.md`](references/checklist.md): anti-patterns, code and export, scientific logic, and final rendering.

<details>
<summary><strong>Repository structure</strong></summary>

```text
academic-data-visualization/
├── SKILL.md                 # Concise decision entry point and on-demand routing
├── AGENTS.md                # Architecture, generated-file, and validation rules
├── agents/openai.yaml       # Codex display and default-prompt metadata
├── references/              # Registry, 24-category catalogue, journals, colour, export, and QA
├── scripts/                 # Generation, validation, composition, colour, and grayscale tools
├── tests/                   # Taxonomy, routing, and generated-output regression tests
├── assets/                  # Production scripts, manifests, atlas, and palette previews
└── install/                 # Codex / Claude Code / Cursor / Copilot adapters
```

</details>

## Contributing and licence

Register the canonical record, aliases, categories, and real implementation state before adding a chart, then run the catalogue generator. A chart may be marked `production_template` only when its real script, PNG, and `asset.yaml` are committed together. Never fabricate previews or asset paths for unimplemented charts. See [`AGENTS.md`](AGENTS.md) for the complete rules.

Licensed under [Apache-2.0](LICENSE).
