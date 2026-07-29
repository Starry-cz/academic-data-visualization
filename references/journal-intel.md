# Journal-Specific Unwritten Preferences

This file contains optional, experience-based routing heuristics. It is not an acceptance checklist and must never override official author instructions, the evidence, or a specific editor's request. Treat every statement below as a hypothesis to verify against current published examples and the target journal guide.

## Operational Journal Style Routing

Use this table only after the user names a target journal or publication context. It converts the journal brief into a reproducible starting point; it does **not** reproduce a journal's branded appearance or override the user's palette choice.

| Target context | Starting theme | Layout and colour direction | Mandatory safeguard |
|---|---|---|---|
| Nature Genetics / genetics-heavy main figure | `teal-genome` | Cool blues/teals for primary evidence; one muted warm accent; dense panels must retain readable labels | Keep a scientific zero for effect heatmaps and never use rainbow chromosomes |
| Nature Plants / photo + quantitative figure | `sage-methods` | Muted greens and warm sand; photo panels establish biological context before quantification when that is the evidence order | Preserve treatment-to-colour mapping across photos, plots, and captions; scale bars remain factual annotations |
| Cell Systems / computational biology | `method-blueprint` for data, `quiet-atlas` for schematic context | Key data use restrained blue; schematics remain quieter than quantitative evidence | Do not assign biological meaning to decorative schematic colours; map network size/width to declared quantities |
| General ML benchmark or ablation | `method-blueprint` or `ablation-contrast` | Blue for the predeclared focal method, green for a positive variant only when scientifically justified, warm colour for an explicit comparator | Never imply superiority through colour alone; report the metric, split, uncertainty, and baseline definition |
| No target journal or cross-disciplinary first proof | `nature-default` | Accessible baseline with stable semantic roles | Keep shapes, labels, or line types for any critical distinction |

### Routing procedure

1. Read the named journal section below and choose the matching row above.
2. Record `journal profile`, `theme`, and each semantic colour role in the five-line design brief before code is written.
3. A user-selected named theme, custom hex set, or reference palette always takes precedence over the suggested starting theme.
4. In the QA report, state whether the final theme is the routed starting theme or a user override. Confirm that the override did not change data, statistics, panel order, or scientific meaning.

The routing table is a style baseline, not an authority on journal acceptance. Official author instructions and the target manuscript's data requirements always prevail.

---

## Nature Genetics

**Overall Figure Style:**
- Strong preference for multi-panel, information-dense figures (Nature Genetics readers expect comprehensive genetic evidence per figure)
- Each main figure typically tells one complete genetic story arc: discovery → validation → mechanism → clinical relevance
- Panel labels (a, b, c...) should follow a clear reading order — the narrative line between panels should be obvious without reading the caption

**Color Preferences:**
- Favor cool-toned palettes (blues, teals, purples) for primary data. Warm colors (red, orange) reserved for emphasis
- Manhattans: prefer dark blue alternating chromosomes, never rainbow chromosomes
- GWAS/heatmap: use diverging blue-white-red (RdBu or custom equivalent), but the red extreme should be muted (not pure #FF0000)

**Figure Caption Expectations:**
- More technical detail expected than other Nature journals. Define every abbreviation, every statistical test used, every data transformation

**Common Desk Reject Triggers:**
- Figures that tell multiple unrelated stories in one composite (sign of weak narrative focus)
- Manhattan plots without clear significance threshold line and annotation of top hits
- Heatmaps where row/column labels are illegible from overcrowding

---

## Nature Plants

**Overall Figure Style:**
- Photographic panels (plant phenotypes, micrographs, tissue sections) must share visual language with data panels
- If a figure mixes photos and data plots, the photo panels typically come first (left to right, top to bottom), establishing the biological context before the quantitative analysis

**Unwritten Rules for Micrographs:**
- Scale bars: minimum length of ~10% of the image width; white or black depending on background; always described in caption
- Magnification must be stated in caption, not just scale bar length
- Fluorescence merge panels: always include individual channel panels alongside the merge (not just the merge in main figure and channels in supplement)

**Figure Caption Expectation:**
- Similar technical rigor to Nature Genetics, but emphasis on describing the biological material (genotype, growth conditions, developmental stage)

**Common Desk Reject Triggers:**
- Microscopy images without scale bars (instant rejection from reviewers)
- Data plots using default Excel/Prism styling (Nature Plants expects polished, custom-styled figures)
- Inconsistent color mapping for the same treatment across different panels

---

## Cell Systems

**Overall Figure Style:**
- Computation/modeling-focused journal — figures must communicate both biological insight AND computational methodology clearly
- Cartoon/schematic diagrams are expected and encouraged (unlike Nature Genetics where they're secondary)
- Schematic panels typically use muted non-data colors (greys, light blues) distinct from data panel colors

**Unwritten Rules:**
- Network and interactome diagrams: node size and edge thickness must be mapped to quantitative properties (never arbitrary), with the mapping explained in caption
- t-SNE/UMAP figures: color scales must be perceptually uniform; label clusters with biologically meaningful names, not numbers
- Model performance plots: prioritise held-out or external performance, show uncertainty across valid resamples, and include calibration or decision utility when the claim requires it. Training performance may be shown only when clearly separated and scientifically useful.

**Common Desk Reject Triggers:**
- Figure overload — trying to cram data + schematic + model diagram into one undersized panel set
- Default R plotting aesthetics (base R plot() output clearly visible)
- Missing statistical details in methods/models described in figures

---

## Adding New Journals

When adding a new journal entry, follow this template:

```markdown
## [Journal Name]

**Overall Figure Style:**
[2-3 sentences about what characterizes this journal's visual style]

**Unwritten Rules:**
- [Specific rule with rationale]

**Common Desk Reject Triggers:**
- [Trigger item]

**Figure Caption Expectation:**
[Any special expectations for captions]
```

Sources: accumulated from published papers, editorial guidelines, and author experiences. Update as new patterns emerge from revision cases (see `revision-cases.md`).
