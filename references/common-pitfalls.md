# Common Pitfalls Across All Figure Types

These are mistakes that signal "not designed" to reviewers, regardless of the specific chart type.

## Default Color Palettes

```
⚠️ matplotlib / seaborn / ggplot2 / Excel defaults used without reviewing semantics, contrast, and grayscale
❌ jet / rainbow colormap for continuous data

✅ A documented palette selected for the variable type and viewing context (custom hex is not automatically better)
✅ Semantic colours whose roles are declared for this study and remain stable across panels
✅ Perceptually uniform sequential colormaps (viridis, cividis, scico)
```

**Why reviewers flag this:** An unreviewed palette can obscure ordering, fail in grayscale, or assign inconsistent meaning. Jet/rainbow maps have non-monotonic luminance and can distort perceived patterns. A default palette may be retained only after it passes the same semantic, contrast, colour-vision, and grayscale review as a custom one.

## Over-Decorated Axes

```
❌ Full four-sided border with grey background grid (ggplot2/seaborn default)
❌ Thick axis spines competing with data for visual attention
❌ Heavy gridlines at major AND minor ticks

✅ Left + bottom spines only, thin (0.5-0.6 pt)
✅ No background grid, or very light guide lines (alpha ≤ 0.3)
✅ Ticks facing outward, not inward (inward ticks can overlap data at plot edges)
```

## Legend Problems

```
❌ Legend floating inside the plot area, occluding data points
❌ Legend with default border and background fill
❌ Redundant legend entries (all groups look identical)

✅ Legend outside plot area (bbox_to_anchor) or direct labeling
✅ Legend with no border, transparent background
✅ Merge redundant legend items; use direct annotation for key features
```

## Font & Typography Issues

```
❌ Default matplotlib font (DejaVu Sans) — looks unpolished in print
❌ Variable font sizes across panels in multi-panel figures
❌ Text rendered at display size then scaled down → illegible at print size
❌ Mixed serif and sans-serif fonts in the same figure

✅ Explicitly set Arial/Helvetica/Liberation Sans
✅ Consistent font sizes within and across panels
✅ Design at print dimensions from the start
```

## Export Mistakes

```
❌ Screenshot or low-resolution PNG as the only deliverable
❌ Rasterized text (text rendered as pixels in a PNG, then placed in a PDF)
❌ PDF with fonts outlined as paths (uneditable)

✅ Vector format (PDF/SVG/EPS) for line art and text
✅ RGB PNG proof at 450 dpi as companion, not as master
✅ Embed fonts properly (see export-specs.md)
```

## Multi-Panel Mistakes

```
❌ Inconsistent panel sizes within the same figure
❌ Missing or inconsistent panel labels (a, b, c...)
❌ Different color scales used for the same variable across panels
❌ Panel spacing so tight that borders merge

✅ Consistent panel dimensions via gridspec/subplot layout
✅ Panel labels in consistent position (top-left of each panel), bold, 8-9 pt
✅ Shared color scale via explicit vmin/vmax or colorRamp2
✅ Adequate spacing (wspace=0.3, hspace=0.3 minimum)
```

## Colorblind Accessibility

```
❌ Red-green as the only distinguishing color pair
❌ No alternative visual channel (only color differentiates categories)

✅ Use blue-orange, blue-purple, or other colorblind-safe pairs
✅ Add shape or linetype as secondary differentiator for critical comparisons
✅ Test with a colorblind simulator
```

## Statistical Display Traps

```
❌ Bar charts hiding individual data points (show points over bars)
❌ Error bars without explanation (SD? SEM? CI?)
❌ Asterisks without threshold definition in deliverable notes
❌ Log scales not explicitly noted on axis or in caption

✅ Overlay individual data points on bar charts (strip plot + bar)
✅ Clarify error bar type in deliverable notes
✅ Prefer exact p-values; define asterisk thresholds if used
✅ Label log-scaled axes as "log10(Expression)" not just "Expression"
```

## Unit-of-Analysis and Inference Traps

```
❌ Treating cells, images, repeated time points, or CV folds as independent biological samples
❌ Reporting only significance stars while hiding effect size and uncertainty
❌ Claiming causality, superiority, or generalisation from a design that supports only association
❌ Showing training performance as if it were held-out performance

✅ Define n and the independent experimental unit in the caption or notes
✅ Prioritise effect size and confidence intervals; retain exact p-values where useful
✅ Match the headline and annotation language to the study design
✅ Separate train/validation/test results and report resampling variation
```

## Axis and Transformation Traps

```
❌ Truncated bar baselines, hidden axis breaks, or aspect ratios chosen to magnify slopes
❌ Diverging colour maps centred at the sample midpoint rather than a meaningful scientific reference
❌ Log transformations applied to zero/negative values without an explicit rule
❌ Independent facet scales that invite direct visual comparison without clear labels

✅ Start bars at zero; make any justified break unmistakable
✅ Centre diverging scales on a declared reference such as zero or a clinical threshold
✅ Record transformations and show interpretable tick labels
✅ Share scales for direct comparisons or label free scales prominently
```

## Image and Processing Integrity

```
❌ Selective contrast, smoothing, cropping, or removal applied to only one comparison group
❌ Microscopy without a scale bar or inconsistent display ranges across comparable images
❌ Undisclosed lane splicing or omitted original image evidence

✅ Apply documented global processing consistently within a comparison
✅ Preserve scale bars, acquisition context, and identical LUT/range where comparison requires it
✅ Disclose splices and retain traceable source images
```

## Product-Launch and Keynote Traps

```
❌ Copying a dense journal panel onto a 16:9 screen
❌ Replacing uncertainty, denominators, or baselines with a marketing slogan
❌ Using motion, rescaling, or selective reveals to exaggerate improvement

✅ Derive a screen-specific view from the same analysis output
✅ Use one supported takeaway, direct labels, large type, and a visible source/method note
✅ Keep scales and semantic mappings stable across animated frames
```
