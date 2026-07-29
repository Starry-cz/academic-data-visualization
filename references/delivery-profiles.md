# Delivery Profiles

Choose the viewing context before selecting canvas, typography, density, and export settings. A chart that works at 89 mm in a paper is not automatically readable on a conference screen.

## 1. Select exactly one primary profile

| Profile | Intended reading | Design baseline | Required deliverables |
|---|---|---|---|
| `journal_print` | Close reading in a manuscript or PDF | Final journal column width; compact but complete labels; caption carries methods detail | Editable PDF/SVG master when appropriate, RGB raster proof at the target specification, grayscale proof, QA report |
| `keynote_screen` | Distant reading in a lecture, conference, or product launch | 16:9-safe chart canvas; one declarative takeaway; few series; direct labels; substantially larger type and marks | SVG/PDF master, 1920×1080 or 3840×2160 RGB PNG, light/dark-background proof as needed, source/method note |
| `report_web` | Laptop or report reading | Responsive 4:3 or wide canvas; concise title; accessible labels and alt text | SVG plus 2× PNG, alt text, source/method note |
| `poster_large` | Reading at roughly 1–2 metres | Physical panel size fixed first; short labels; strong hierarchy; no manuscript-sized text | PDF/SVG master and full-size raster proof at the printer specification |

If the final medium is unknown, use `journal_print` only for a manuscript request. For a talk, launch, or presentation request, use `keynote_screen`. Do not design one compromise file for both; derive separate exports from the same data and semantic mapping.

## 2. Journal profile

- Verify the named journal’s current instructions instead of assuming one universal Nature/Cell/Science template.
- Set final physical dimensions before judging type, line, and marker size.
- Preserve editable text and line work. Rasterize only genuine images or data-heavy layers.
- Use axes, ticks, units, uncertainty, sample size, and statistical definitions required to interpret the claim.
- Treat 300 dpi as a common minimum for genuine raster images, not as a substitute for vector line art. A 450 dpi proof is useful for inspection and is compatible with Nature’s online-proof guidance, but it is not a universal requirement for every publisher or content type.

## 3. Keynote and product-launch profile

This profile creates the **data-visualization asset**, not an entire slide deck.

- Write a one-sentence takeaway headline that states the supported result, not a slogan that overclaims it.
- Show one primary comparison per chart. Move secondary analyses to another chart rather than shrinking them into unreadable insets.
- Prefer direct labels, endpoint labels, and short annotations. Remove legends only when the chart remains unambiguous.
- Use a 16:9-safe composition with generous margins. Test at both full screen and a reduced thumbnail.
- Use screen-readable type. As a starting point on a 1920×1080 canvas, use approximately 28–36 px for labels, 36–48 px for annotations, and 48–64 px for the takeaway; then verify at the actual venue and viewing distance.
- Keep no more than three or four decision-relevant series in one view. Use muted context plus one accent for the focal evidence.
- Include a compact source/method note and define non-obvious metrics. Never remove uncertainty, denominators, baselines, or time windows merely to make a cleaner launch graphic.
- For dark backgrounds, re-check text contrast, thin strokes, gridlines, and colour meanings; do not invert a journal palette mechanically.
- If animation is requested, keep axes and encodings stable across frames. Use reveals to explain sequence, never to conceal unfavourable values or create a false change in scale.
- Export at the exact stage resolution when known. Otherwise provide SVG/PDF plus 1920×1080 and 3840×2160 PNG versions.

## 4. Accessibility requirements

- Do not use colour as the only carrier of a critical distinction.
- For screen profiles, target WCAG 2.2 AA text contrast: at least 4.5:1 for normal text and 3:1 for large text.
- Meaningful graphical objects and adjacent states should normally reach 3:1 contrast or use a border, shape, line style, direct label, or spacing that conveys the same information.
- Supply concise alt text that states the chart type, comparison, direction, and main quantitative result. Provide a longer description or accessible data table when the chart contains details that cannot fit in alt text.
- Inspect colour-vision simulations and a grayscale proof; simulation alone does not replace redundant encoding.

## 5. Integrity invariant across profiles

Changing profile may change canvas, type size, annotation density, and panel count. It must not change:

- source values, exclusions, transformations, or group order;
- axis baseline or scale without explicit disclosure;
- uncertainty, denominator, sample definition, or statistical result;
- semantic colour roles;
- the strength or direction of the supported claim.

If a screen version must simplify a journal figure, keep a traceable mapping from every displayed value to the same analysis output used by the manuscript figure.

## Sources

- Nature Research Figure Guide: <https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>
- IEEE graphics resolution and size: <https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/>
- W3C WCAG 2.2 non-text contrast: <https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast>
- Tableau visual best practices: <https://help.tableau.com/current/pro/desktop/en-us/visual_best_practices.htm>
