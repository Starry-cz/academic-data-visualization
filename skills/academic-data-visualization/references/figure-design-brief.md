# Figure Design Brief: Layout, Hierarchy, and Colour Roles

Use this reference before code is written for every figure with two or more panels. It turns a visual intention into constraints that can be checked after rendering.

## 1. Write the design brief in five lines

```text
Canvas: [single / double column] · [4:3 / 3:2 / wide] · [target final width]
Core message: [one sentence]
Journal profile: [journal / target context] · [routed theme or user override]
Hierarchy: [equal grid, or hero panel + its evidence-based reason]
Support sequence: [(b) → (c) → …, each adds a non-redundant evidence step]
Colour roles: [baseline, comparison, emphasis, context]
```

- Decide the aspect ratio before building panels. Use `4:3` for compact quantitative grids, `3:2` for a balanced main figure, and `wide` only when the scientific sequence truly runs horizontally.
- Use equal panels for parallel evidence. Give a justified hero panel 1.2–1.5× the area of a support panel only when it carries the decisive result or necessary overview. Do not enlarge a panel merely because it has more labels.
- Keep the canvas white, use quiet neutral axes, and reserve the accent for one evidence role rather than every panel.
- When a target journal is named, read `references/journal-intel.md` and record the routed starting theme or a user override. Journal style informs hierarchy and palette restraint; it never changes evidence, statistics, or data encoding.

## 2. Reusable composition recipes

| Recipe | Best fit | Layout rule | Narrative order |
|---|---|---|---|
| `evidence-grid` | Four comparable quantitative results | 2×2 equal panels; consistent axes and margins | overview → comparison → robustness → validation |
| `hero-plus-proof` | One decisive map, UMAP, heatmap, image plate, or model output | hero occupies 1.2–1.5× area; two to four smaller proofs align to its edge | main result → mechanism / stratification → validation |
| `workflow-to-result` | Cohort, multi-modal, or methods figures | compact schematic plus 2–3 data panels; schematic never displaces core evidence | schematic first only when needed to decode measurements; otherwise evidence first |
| `landscape-comparison` | Benchmarks, ablations, or time series | shared baseline across a horizontal sequence; direct labels at line ends | benchmark → difference → uncertainty / sensitivity |
| `benchmark-strip` | Three or more metrics, methods, or ablation blocks | use a width/height ratio of 2.6–4.0; add a dedicated legend cell when labels cannot fit outside | reference → proposed / variants → robustness |

For `workflow-to-result`, place a schematic first only if it is essential to decode the measurements. Otherwise put empirical evidence at (a) and the explanatory schematic later.

### Legend decision rule

1. Prefer direct labels when there are at most three readable lines or groups.
2. Place a compact legend outside the data area when it fits without shrinking the panel.
3. For four or more series, repeated method names, or a multi-metric `benchmark-strip`, reserve one small legend-only cell. Turn its axes off and collect handles from the data panels. Never overlay a large legend on evidence merely to preserve a symmetric grid.
4. When categories are identified entirely by a shared legend and panel title, hide repeated x-tick names only if this does not make a standalone panel ambiguous.

## 3. Palette roles, not palette decoration

1. Use no more than 2–4 full-saturation categorical colours per panel; soften secondary evidence with alpha or neutral context.
2. Keep `categorical[0]` as the baseline and use `accent` for only one predeclared role (for example, treatment, selected subgroup, or a key threshold).
3. Use a sequential ramp only for ordered magnitude, and a diverging ramp only when the midpoint is scientifically meaningful.
4. For a dense figure, prefer one muted primary family plus one warm accent. Never use every palette colour simply because it is available.
5. Preserve the same semantic colour mapping in the whole figure and in all supplementary panels.

## 4. Pre-export visual audit additions

After the automatic `visual_qa.py` gate passes, inspect the rendered figure at intended display size:

- Is the title, panel label, legend, and annotation hierarchy obvious in three seconds?
- If a hero panel is declared, does it dominate for an evidence-based reason? If the grid is equal, are panel weights genuinely comparable?
- Is there enough whitespace between panels for labels, colour bars, and direct line labels?
- Does each accent colour identify one concept consistently, rather than competing for attention?
- Can the reader follow the panels left-to-right without jumping back to a legend?
- Does the grayscale proof preserve every decision-relevant comparison through luminance or a redundant non-colour encoding?

If any answer is no, revise the composition or colour roles and run the mandatory render gate again before exporting.

## Design reference note

This guide independently translates useful high-level ideas from public figure resources into reproducible plotting constraints: curated examples, early aspect-ratio decisions, strong panel hierarchy, restrained literature-style colour roles, journal-aware style baselines, dense-but-scannable composition, reserved legend space for complex comparisons, and a rendered grayscale proof rather than a palette-only accessibility claim. It does not reuse their scripts, prompts, or generated images. References: <https://github.com/wuyoscar/GPT-Image2-Skill#gallery-research-paper-figures>, <https://github.com/ChenLiu-1996/figures4papers>, <https://github.com/TingxiYu/academic-figure-skill>, and <https://github.com/Haojae/scipilot-figure-skill>.
