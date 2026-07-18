# Theme Library and Accessible Colour System

This skill has one default theme and fourteen user-selectable themes extracted from the supplied scientific figure references. The palette library is intentionally a **style layer**, not a change to scientific meaning: preserve category order, statistical markings, and mark types whenever a theme changes.

## Select a theme

| ID | Theme | Best fit | Categorical colours |
|---|---|---|---|
| `nature-default` | Nature 默认 **(default)** | General publication figures and first proofs | `#0072B2 #009E73 #E69F00 #CC79A7 #D55E00 #56B4E9` |
| `vivid-signal` | 高辨识信号 | Small group counts, strong highlights | `#E31A1C #FC8D3C #377EB8 #984EA3 #4DAF4A` |
| `bright-bio` | 明亮生物 | Multi-condition molecular biology panels | `#F7A63A #557CFF #80C662 #866AD2 #56BFB0` |
| `teal-genome` | 青绿组学 | Genomics and network-style pages | `#0F9EA8 #008B82 #45728F #8CD1B2 #8B84A3` |
| `muted-microbe` | 柔和微生物 | Experimental biology and culture studies | `#BA4460 #FFAFAC #DBAC72 #87AD7C #65AA93` |
| `immuno-signal` | 免疫信号 | Immune-response contrasts | `#A9C4E2 #B9D6ED #AEDFE4 #F04A4D #5896D0 #68C9D4` |
| `pastel-catalysis` | 粉彩催化 | Materials and catalytic comparisons | `#7AD4FE #FDCBA7 #B3DDD4 #C9D2F9 #DDEAF6` |
| `electrochemistry` | 电化学柔彩 | Electrochemistry and environmental series | `#E26E67 #509CBA #91BFDB #F1B9B6 #A4D86A` |
| `soft-cost` | 柔和成本 | Techno-economic and process comparisons | `#6DA4B0 #ABCBD4 #E1B3AD #D78F81 #D7CDE1` |
| `soft-academic` | 柔和学术 | Multi-panel academic reports and talks | `#FCE8E6 #FFC6BC #F8B9B8 #D6DFEF #A5CDE2 #5FA3CB` |
| `pastel-omics` | 柔彩组学 | Multi-cohort omics and population-structure panels | `#F9ADE5 #EFEAB7 #BBD6F5 #AAD1CC #C0A3ED #F6B593` |
| `warm-cool-kinetics` | 暖冷动力学 | Half-life, decay-rate, and time-resolved molecular panels | `#D7312D #F2724D #FEE395 #FEF9B7 #ACD2E5 #6090C1` |
| `aquifer-recovery` | 含水层复苏 | Hydrogeology, climate, and recovery trajectories | `#F599A1 #9FD7E9 #95AEDA #FCD590 #A577AD #73C79E` |
| `neuro-navy` | 神经深蓝 | Neuroscience contrasts and intervention comparisons | `#D9E6EB #9FC3D5 #8F96BD #2A347A #D6D69B` |
| `cryo-electrolyte` | 低温电解质 | Electrolytes, low-temperature materials, and stability panels | `#ECE3EF #CFBBD9 #D9EBF2 #A2D1E6 #F9CFB1 #355AA4` |

The canonical full values, including sequential and diverging ramps, live in [`palette-library.json`](palette-library.json). Use that file as the single source of truth for preview scripts and future adapters.

### Selection and personalization protocol

1. Before drawing, use the user's named theme; otherwise use `nature-default` and say so in the initial plan.
2. Keep one semantic mapping across all panels: `categorical[0]` is the baseline, following entries are ordered comparisons, `accent` is a single emphasis role, and grey/neutral is context.
3. After the QA-passed first proof, ask whether the user wants a different library theme, explicit hex colours, or a reference palette image.
4. For a supplied palette image, first return the inferred swatches and proposed semantic order for confirmation. Recolour only after confirmation; do not change data, analyses, figure type, or statistical annotations.
5. Named themes are aesthetic choices, not universal accessibility guarantees. Keep shapes, line types, direct labels, or ordering for critical comparisons; use `nature-default` when colourblind-safe categorical distinction is the primary requirement.

## Nature-ready Accessible Colour System

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
