# Figure Design Brief: Layout, Hierarchy, and Colour Roles

Use this reference before code is written for every figure with two or more panels. It turns a visual intention into constraints that can be checked after rendering.

## 1. Write the design brief in five lines

```text
Canvas: [single / double column] · [4:3 / 3:2 / wide] · [target final width]
Core message: [one sentence]
Hero panel: [(a), its evidence, and why it is visually dominant]
Support sequence: [(b) → (c) → …, each adds a non-redundant evidence step]
Colour roles: [baseline, comparison, emphasis, context]
```

- Decide the aspect ratio before building panels. Use `4:3` for compact quantitative grids, `3:2` for a balanced main figure, and `wide` only when the scientific sequence truly runs horizontally.
- Give the hero panel 1.2–1.5× the area of a support panel. Do not enlarge a panel merely because it has more labels.
- Keep the canvas white, use quiet neutral axes, and reserve the accent for one evidence role rather than every panel.

## 2. Reusable composition recipes

| Recipe | Best fit | Layout rule | Narrative order |
|---|---|---|---|
| `evidence-grid` | Four comparable quantitative results | 2×2 equal panels; consistent axes and margins | overview → comparison → robustness → validation |
| `hero-plus-proof` | One decisive map, UMAP, heatmap, image plate, or model output | hero occupies 1.2–1.5× area; two to four smaller proofs align to its edge | main result → mechanism / stratification → validation |
| `workflow-to-result` | Cohort, multi-modal, or methods figures | compact schematic plus 2–3 data panels; schematic never displaces core evidence | data / outcome first → method synthesis → practical interpretation |
| `landscape-comparison` | Benchmarks, ablations, or time series | shared baseline across a horizontal sequence; direct labels at line ends | benchmark → difference → uncertainty / sensitivity |

For `workflow-to-result`, place a schematic first only if it is essential to decode the measurements. Otherwise put empirical evidence at (a) and the explanatory schematic later.

## 3. Palette roles, not palette decoration

1. Use no more than 2–4 full-saturation categorical colours per panel; soften secondary evidence with alpha or neutral context.
2. Keep `categorical[0]` as the baseline and use `accent` for only one predeclared role (for example, treatment, selected subgroup, or a key threshold).
3. Use a sequential ramp only for ordered magnitude, and a diverging ramp only when the midpoint is scientifically meaningful.
4. For a dense figure, prefer one muted primary family plus one warm accent. Never use every palette colour simply because it is available.
5. Preserve the same semantic colour mapping in the whole figure and in all supplementary panels.

## 4. Pre-export visual audit additions

After the automatic `visual_qa.py` gate passes, inspect the rendered figure at intended display size:

- Is the title, panel label, legend, and annotation hierarchy obvious in three seconds?
- Does the hero panel still dominate without oversized text or a heavy border?
- Is there enough whitespace between panels for labels, colour bars, and direct line labels?
- Does each accent colour identify one concept consistently, rather than competing for attention?
- Can the reader follow the panels left-to-right without jumping back to a legend?

If any answer is no, revise the composition or colour roles and run the mandatory render gate again before exporting.

## Design reference note

This guide independently translates the useful high-level ideas from the GPT-Image2-Skill research-figure gallery—curated examples, early aspect-ratio decisions, strong panel hierarchy, restrained literature-style colour roles, and dense-but-scannable composition—into reproducible plotting constraints. It does not reuse its prompts or generated images. Reference: <https://github.com/wuyoscar/GPT-Image2-Skill#gallery-research-paper-figures>.
