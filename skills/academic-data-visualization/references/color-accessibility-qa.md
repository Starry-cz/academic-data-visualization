# Rendered Colour Accessibility QA

Use this reference when reviewing colour legibility, white-background readability, opacity, grayscale separation, or a colour-related QA warning.

## Scope

The colour gate has two layers. Keep them separate:

1. **Palette provenance** checks whether the declared theme is an exact registered theme.
2. **Rendered appearance** checks the colours that are actually present in the final SVG after opacity is composited over the exported background.

Passing palette provenance does not prove that a chart is readable. A registered pale colour may be suitable for a confidence band or panel background but unsuitable for text, a primary line, or a small point.

## Compatibility contract

Existing commands, palette values, theme routing, renderer output, and check IDs remain valid.

- Default mode is `compatible`: newly detected rendered-colour problems are reported as `WARN`, so historical templates do not become unrunnable merely because the checker was upgraded.
- `--strict-colors` promotes low-contrast rendered text and essential graphical objects to `FAIL`.
- The checker never changes a colour, alpha value, theme, or chart automatically.
- Uncertainty bands remain review warnings because they may intentionally provide low-contrast context; their boundary or central estimate must carry the essential evidence.

Use strict mode for new figures, materially revised figures, and final delivery:

```bash
python scripts/qa_validator.py \
  --output-dir output/figure \
  --manifest templates/production-verified/<chart-id>/asset.yaml \
  --strict-colors
```

## Checks

| ID | Input | Meaning | Threshold and action |
|---|---|---|---|
| `COLOR-1` | Metadata | Declared theme exactly matches the registered palette library | Existing hard gate; unchanged |
| `A11Y-1` | Metadata | All declared theme colours against white | Existing 3:1 advisory; unchanged, including colours not used in the figure |
| `COLOR-2` | Final SVG | Actual essential graphical marks against the explicit canvas background | 3:1 after alpha compositing; `WARN` in compatible mode, `FAIL` in strict mode |
| `A11Y-3` | Final SVG | Actual text against the explicit canvas background | 4.5:1 after alpha compositing; `WARN` in compatible mode, `FAIL` in strict mode |
| `COLOR-3` | Final SVG | Low-contrast uncertainty/context bands | Manual-review warning; the band must not be the only evidence |
| `A11Y-4` | Final SVG + metadata | Rendered categorical colours with very similar grayscale luminance | Manual-review warning; verify markers, line styles, hatches, labels, position, or ordering |
| `COLOR-4` | Final SVG | Solid-paint parsing coverage | Warns when gradients, paint servers, embedded raster/image layers, or unresolved colours need visual inspection |
| `COLOR-5` | Final SVG | Low-opacity graphical context below 3:1 | Manual-review warning; confirm these marks are contextual rather than the only evidence |
| `A11Y-5` | Final SVG | Text whose colour matches the canvas and may sit on a local dark cell | Manual-review warning because cell-level overlap is not inferred |

## Role rules

- Text is evaluated as text, not as a generic palette swatch.
- Matplotlib canvas and axes backgrounds are excluded from data-mark checks.
- Axes and tick scaffolding are classified separately from evidence marks.
- `FillBetweenPolyCollection` is treated as uncertainty context, not as the primary series.
- Other visible fills and strokes are treated as graphical objects unless the SVG identifies a more specific role.
- Strokes at opacity `>= 0.75` and fills at opacity `>= 0.60` are treated as essential candidates. Lower-opacity graphical marks are reported separately for role confirmation.
- The exported canvas background must be explicit. If it is absent, the checker reports that contrast could not be established instead of guessing white.

## Opacity rule

Always evaluate the colour seen by the reader, not the raw hex value. For foreground `F`, background `B`, and opacity `a`, the checker first computes:

```text
visible = a × F + (1 - a) × B
```

It then computes contrast using the visible colour. This catches marks that use an acceptable dark source colour but become unreadable after `alpha=0.1` or `fill-opacity=0.2` on white.

## Required human review

Automated colour checks cannot prove the following:

- whether neighbouring marks overlap in the exact region where contrast matters;
- whether heatmap annotation text contrasts with the local cell rather than the page background;
- whether a low-luminance-difference pair is safely distinguished by marker, line style, hatch, label, or position;
- whether the figure remains readable at final print size, projector distance, or in a screenshot thumbnail;
- whether colour semantics stay stable across a multi-panel manuscript.

Therefore strict colour QA complements, but does not replace, the final-size RGB and grayscale review in `references/visual-review-protocol.md`.

## Fix order

When a check fails, repair in this order:

1. Increase text or primary-mark contrast against the actual background.
2. Reduce unnecessary transparency on essential marks.
3. Add direct labels, marker shapes, line styles, hatches, or ordering.
4. Reassign an existing registered theme colour to the correct semantic role.
5. Change the palette library only through a separately approved palette revision.

Do not solve contrast by silently changing the registered palette or by making uncertainty bands visually dominate the central estimate.
