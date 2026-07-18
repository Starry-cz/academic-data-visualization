# Nature-ready Accessible Colour System

Nature does not prescribe one universal set of hex codes. Its figure guide requires an accessible palette and points authors to Wong's colour-blindness guidance. This system therefore uses a colour-blind-safe qualitative core, then creates restraint with alpha, ordering, and neutral context—not with low-contrast category colours. Source: <https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>.

> **BASELINE — COPY VERBATIM:** Put the applicable block at the top of every generated plotting script. Assign colours by semantic role and keep that mapping identical across panels.

```python
# Academic Data Visualization — Nature-ready accessible palette
# 使用色盲安全主色；低对比度信息通过透明度和中性灰处理，而不是新增相近色。
CATEGORICAL = ["#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9"]
CATEGORICAL_EXTENDED = [
    "#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9", "#999999"
]
DIVERGING = ["#2166AC", "#F7F7F7", "#B2182B"]
SEQUENTIAL = ["#F7FBFF", "#C6DBEF", "#6BAED6", "#2171B5", "#084594"]
ACCENT = "#D55E00"
INK = "#1A1A1A"
GREY = "#6B7280"
GRID = "#D7DEE6"  # 仅在确有读数需要时使用极淡主网格。
BACKGROUND = "#FFFFFF"
```

```r
# Academic Data Visualization — Nature-ready accessible palette
categorical <- c("#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9")
categorical_extended <- c(
  "#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9", "#999999"
)
diverging <- c("#2166AC", "#F7F7F7", "#B2182B")
sequential <- c("#F7FBFF", "#C6DBEF", "#6BAED6", "#2171B5", "#084594")
accent <- "#D55E00"
ink <- "#1A1A1A"
grey <- "#6B7280"
grid <- "#D7DEE6"
background <- "#FFFFFF"
```

## Semantic Assignment

| Role | Colour | Use |
|---|---|---|
| Primary evidence / baseline | Blue `#0072B2` | Reference condition, primary trend, focal category. |
| Secondary comparison | Bluish green `#009E73` | Parallel condition or second cohort. |
| Third comparison | Orange `#E69F00` | A distinct category; never use as warning by default. |
| Fourth comparison | Purple `#CC79A7` | Independent lineage or model family. |
| Directional emphasis | Vermillion `#D55E00` | Selected finding, adverse direction, threshold hit; one emphasis role per panel. |
| Support / low priority | Sky `#56B4E9` or grey `#999999` | Context, non-significant points, secondary trace. |

## Rules That Survive Greyscale

- Use 2–4 categorical colours by default. For more than six groups, facet, order, or directly label rather than add hues.
- Never use red and green as the only distinction. Add a marker shape, line type, ordering, faceting, or direct label for every critical comparison.
- Keep category-to-colour mapping stable across panels and across figures in one manuscript.
- Use black or near-black text. Do not use coloured legend text; pair black text with a coloured key.
- Use alpha `0.18–0.35` for confidence bands and dense background points; keep the focal mark opaque.

## Continuous and Diverging Data

- **Correlation, effect direction, z-score:** use `DIVERGING`; set the neutral midpoint at the scientific zero.
- **Abundance, density, confidence:** use `SEQUENTIAL`; reserve the darkest tone for the largest values.
- **Heatmaps:** use white or very light cell separators. Annotate only decision-relevant cells; do not turn every cell label bold.
- Do not use `jet`, `rainbow`, `hsv`, default `tab10/tab20`, seaborn defaults, ggplot2 hue defaults, or Excel defaults.

## Print and Layout Defaults

- Use a white background and no background grid by default. If a quantitative comparison truly needs guidance, retain only very light major horizontal gridlines (`GRID`, 0.3 pt).
- Draw axes and text in `INK`. Use 0.6 pt axes/ticks, 1.0–1.2 pt data lines, and 0.5–0.8 pt error bars.
- Use solid fills and direct labels; avoid patterned fills, drop shadows, decorative gradients, and heavy outlines.
