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

<p align="center">
  <img src="assets/readme/academic-data-visualization-workflow-v5.png" width="100%" alt="Workflow from research question and data profiling to publication-ready figures and visual review">
</p>

## Why use it

| Claim first | Honest capability boundaries | Reusable production assets | Submission-ready QA |
|---|---|---|---|
| Decide what readers must compare, relate, or judge before choosing a chart | Every one of the 665 canonical records has an explicit implementation state | 34 asset families include scripts, previews, and manifests for traceable reuse | Review anti-patterns, code and export, scientific logic, and the final rendering |

Conventional plotting requests start with “make a bar chart” or “draw a heatmap.” This Skill starts with the scientific claim and data contract, and actively blocks common risks such as small-sample mean bars, dual axes, rainbow maps, invalid connecting lines, and misleading truncation.

## How it works

| Stage | Key action | Output |
|---|---|---|
| 1. Define | Fix the claim, observation unit, variables, dependence, and target journal | [`figure-contract.md`](references/figure-contract.md) |
| 2. Defend | Profile sample sizes, distributions, missingness, outliers, and groups; compare candidates | Chart rationale and risk notes |
| 3. Implement | Route to a production template, reusable pattern, or on-demand build; unify panels and colour | Python / R code and editable master |
| 4. Verify | Run programmatic checks and inspect final-size RGB, grayscale, and export proofs | Proofs, vector files, and QA report |

## Capability scope

<!-- chart-registry:summary:start -->
The registry separates catalogue coverage from implementation status. Only production templates have reusable scripts, previews, and manifests.

<table width="100%" align="center">
  <tr><td width="35%"><strong>Taxonomy categories</strong></td><td>24</td></tr>
  <tr><td width="35%"><strong>Canonical chart records</strong></td><td>665</td></tr>
  <tr><td width="35%"><strong>Source taxonomy records</strong></td><td>625</td></tr>
  <tr><td width="35%"><strong>Repository extensions</strong></td><td>40</td></tr>
  <tr><td width="35%"><strong>Source memberships</strong></td><td>714 / 714 mapped</td></tr>
  <tr><td width="35%"><strong>Production templates</strong></td><td>34</td></tr>
  <tr><td width="35%"><strong>Reusable patterns</strong></td><td>228</td></tr>
  <tr><td width="35%"><strong>On-demand routes</strong></td><td>403</td></tr>
</table>
<!-- chart-registry:summary:end -->

| State | Meaning | Repository promise |
|---|---|---|
| `production_template` | Verified production template | Real script + PNG + `asset.yaml`, with SVG/PDF where available |
| `reusable_pattern` | Reusable implementation pattern | Explicit data contract and backend route, but no claim of a standalone asset |
| `on_demand` | Built for the actual data and dependencies | No fake previews and no look-alike substitutes for specialist charts |

Browse the [complete 24-category catalogue](references/figure-type-catalog.md), [bilingual alias index](references/chart-alias-index.md), [coverage audit](references/chart-coverage-audit.md), and [verified production-asset map](references/directory-map.md).

## Selected figures

The landing page shows six representative examples. Use the [production asset directory](assets/figures/) and [chart catalogue](references/figure-type-catalog.md) for full previews and implementation states.

<table width="100%" align="center">
  <tr>
    <td width="50%" align="center" valign="top"><strong>Correlation matrix</strong><br><img src="assets/figure-atlas/readme-cards/Correlationmatrix.png" width="390" alt="Correlation matrix example"></td>
    <td width="50%" align="center" valign="top"><strong>PCA</strong><br><img src="assets/figure-atlas/readme-cards/PCA.png" width="390" alt="PCA example"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>Violin plot</strong><br><img src="assets/figure-atlas/readme-cards/violin_chart.png" width="390" alt="Violin plot example"></td>
    <td align="center" valign="top"><strong>Time trend</strong><br><img src="assets/figure-atlas/readme-cards/trend.png" width="390" alt="Time trend example"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>Sankey diagram</strong><br><img src="assets/figure-atlas/readme-cards/sankey.png" width="390" alt="Sankey diagram example"></td>
    <td align="center" valign="top"><strong>Mantel correlation</strong><br><img src="assets/figure-atlas/readme-cards/MantelCorrelation.png" width="390" alt="Mantel correlation example"></td>
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
    <td align="center" valign="top"><strong>Pastel harmony</strong><br><img src="assets/palette-gallery/pastel-harmony.png" width="390" alt="Pastel harmony palette preview"></td>
    <td align="center" valign="top"><strong>Coastal sunset</strong><br><img src="assets/palette-gallery/coastal-sunset.png" width="390" alt="Coastal sunset palette preview"></td>
  </tr>
</table>

See [`color-palettes.md`](references/color-palettes.md) and [`palette-library.json`](references/palette-library.json) for complete values, semantic roles, and usage constraints.

## Scope boundaries

| Good fit | Out of scope |
|---|---|
| Manuscript main figures, supplements, theses, and scientific reports | Interactive dashboards or web data products |
| Choosing a defensible chart from the real data structure | Illustration-only mechanisms with no quantitative panels |
| Rebuilding old figures, unifying panels, or adapting to a journal | Statistical analysis, cleaning, or literature review with no figure goal |
| Pre-submission checks for clipping, overlap, grayscale, misleading encodings, and export | Pretending that a generic chart is a map, genome track, or 3D volume |

## Documentation map

| Need | Start here |
|---|---|
| Find a chart, alias, and real implementation state | [Chart catalogue](references/figure-type-catalog.md) · [Alias index](references/chart-alias-index.md) · [Registry](references/chart-registry.yaml) |
| Define inputs, claims, and deliverables | [Figure contract](references/figure-contract.md) · [Design brief](references/figure-design-brief.md) |
| Organise multipanel hierarchy | [Multipanel layout](references/multipanel-layout.md) · [Visual style](references/visual-style.md) |
| Match journal dimensions and export | [Journal intelligence](references/journal-intel.md) · [Journal specs](references/journal-specs.md) · [Export specs](references/export-specs.md) |
| Select or extend a palette | [Colour guide](references/color-palettes.md) · [Palette registry](references/palette-library.json) |
| Reuse assets and run final checks | [Asset reuse protocol](references/asset-reuse-protocol.md) · [Four-pass QA checklist](references/checklist.md) |

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
