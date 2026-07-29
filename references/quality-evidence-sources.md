# Quality Evidence Sources

This file records why the Skill's cross-cutting rules exist. Official publisher and standards sources define requirements; public repositories provide workflow patterns and examples but do not define journal acceptance.

## Authoritative requirements and guidance

| Source | Rule adopted by this Skill |
|---|---|
| [Nature Research Figure Guide](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) | Editable standard sans-serif text, final-size type checks, RGB workflow, accessible colour, restrained decoration, axes/ticks/units, and content-aware raster handling |
| [IEEE Author Center: resolution and size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/) | Vector-first line art, separate raster thresholds by content, and verified one-/two-column dimensions |
| [Cell Press image-integrity guidance](https://crosstalk.cell.com/blog/checking-out-our-figures) | Preserve original image evidence; avoid selective processing; disclose discontinuities and edits |
| [Cell Press graphical abstract guide](https://crosstalk.cell.com/hubfs/Files/GA_guide.pdf) | One clear visual point, sparse text, logical reading order, and no unsupported speculation in summary graphics |
| [W3C WCAG 2.2 non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast) | Screen text and essential graphical elements require measurable contrast or equivalent redundant cues |
| [W3C technique G209](https://www.w3.org/WAI/WCAG22/Techniques/general/G209.html) | Adjacent meaningful colour regions need contrast or a separating border |
| [Matplotlib colormap guidance](https://matplotlib.org/stable/users/explain/colors/colormaps.html) | Prefer perceptually ordered lightness for quantitative scales; avoid rainbow/jet distortions |
| [Matplotlib normalization guidance](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html) | Match normalization to the data and centre diverging scales on a meaningful reference |
| [Seaborn colour-palette tutorial](https://seaborn.pydata.org/tutorial/color_palettes.html) | Select qualitative, sequential, or diverging palettes from the variable semantics and task |
| [Tableau visual best practices](https://help.tableau.com/current/pro/desktop/en-us/visual_best_practices.htm) | Audience and purpose first, clear context and units, logical eye flow, restrained colour, and validation at the intended display size |

## Public repository patterns reviewed

| Repository | Pattern adopted | Boundary |
|---|---|---|
| [figures4papers](https://github.com/ChenLiu-1996/figures4papers) | Show real examples early and pair reusable code with visual outputs | Examples inspire implementation; they do not replace evidence or journal checks |
| [SciPilot Figure Skill](https://github.com/Haojae/scipilot-figure-skill) | Profile data before chart selection, intercept classic mistakes, and close the loop with rendered visual review | This repository retains its own registry, assets, and QA rules |
| [GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | Use curated visual references and explicit composition intent | AI-generated research graphics are references/workflow aids unless their evidence is fully reproducible and verified |

## Policy hierarchy

When sources conflict, apply this order:

1. scientific and data integrity;
2. the target journal/venue's current official instructions;
3. accessibility standards and legal/organisational requirements;
4. the declared delivery profile;
5. repository defaults and visual examples;
6. aesthetic preference.

Never use “Nature style” or “launch style” as permission to change values, hide uncertainty, omit denominators, exaggerate baselines, or imitate another organisation's brand.
