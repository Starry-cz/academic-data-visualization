# Journal Technical Specifications

Starting specifications for submission-oriented figures. They are not universal across Nature, Cell, Science, IEEE, or individual society journals; verify the current instructions for the named target before final export.

## Figure Dimensions

| Layout | Width | Max Height |
|--------|-------|------------|
| Nature single-column baseline | 89 mm (3.5 in) | 247 mm (9.7 in) |
| Nature double-column baseline | 183 mm (7.2 in) | 247 mm (9.7 in) |
| IEEE journal baseline | 88.9 mm (one column) or 182 mm (two columns) | Verify the target journal/template |

- Height limit includes the space before the figure caption
- For multi-panel figures, the total width including panel spacing must fit within these bounds
- Set figure dimensions at creation time — never scale down post-render. Fonts sized for a large canvas will become illegible when shrunk

### Python

```python
mm_to_inch = 1 / 25.4
fig, ax = plt.subplots(figsize=(89 * mm_to_inch, 70 * mm_to_inch))  # single-column
fig, ax = plt.subplots(figsize=(183 * mm_to_inch, 120 * mm_to_inch)) # double-column
```

### R

```r
# Single column
ggsave("figure.pdf", width = 89, height = 70, units = "mm")

# Double column
ggsave("figure.pdf", width = 183, height = 120, units = "mm")
```

## Color Mode

- **Use RGB by default** when the target accepts it; verify the current instructions
- Do NOT assume pure CMYK — journals may convert for print, but RGB output ensures faithful online rendering
- If a journal specifically requests CMYK, convert only at final export (never work in CMYK during design)

## Spines and Axes

- Remove top and right spines when they do not encode a scale or frame required by the chart
- Keep the axes needed to decode values; image plates and matrix plots may require different borders
- Spine linewidth: 0.5-0.6 pt (thinner than data elements)
- Tick direction: outward (`xtick.direction: out`, `ytick.direction: out`)
- Gridlines: remove by default. If needed for reader guidance, use very light grey (`#E0E0E0`, `linewidth=0.3`, `alpha=0.5`)

## Statistical Annotation

- **Prefer exact p-values** over asterisks where space permits (e.g., `p = 0.032`)
- If using asterisks, define thresholds in the figure caption:
  - `*p < 0.05`, `**p < 0.01`, `***p < 0.001`
- Place significance bars or brackets above the data, not overlapping
- For boxplots/violin plots: use compact bracket notation with small font (5-6 pt)

## Linetypes and Markers

| Element | Specification |
|---------|--------------|
| Reference lines (diagonal for ROC/PR, baseline = 0) | Light grey dashed (`color="grey", linestyle="--", linewidth=0.5, alpha=0.5`) |
| Trend lines (regression, loess) | Solid, thicker than data points, matching color scheme |
| Confidence bands | Semi-transparent fill (`alpha=0.15-0.25`) preferred over dense error bars |
| Data point markers | Avoid oversized markers; `s=10-20` for scatter, `ms=3-5` for line plots |

All dimensions, line widths, and marker sizes are starting values at final output size. Validate them on the rendered proof instead of treating a code constant as automatic compliance.

## Official references

- Nature Research Figure Guide: <https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>
- IEEE Author Center, resolution and size: <https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/>
