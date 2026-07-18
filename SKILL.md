---
name: academic-data-visualization
description: >-
  Academic-grade scientific figure creation for Nature/Cell/Science journals. Use when the user asks to create, polish, review, or export scientific figures for manuscript submission. DO NOT trigger for: interactive dashboards (Plotly/Bokeh/Altair), exploratory data analysis without publication intent, math function plots, pie/3D charts, PowerPoint slides, or Illustrator/Figma-first design. SKIP requests about statistical testing, data cleaning, literature review, or code debugging — these are not figure-making tasks.
---

# Academic Data Visualization

Academic Data Visualization generates publication-grade scientific figures for Nature/Cell/Science family journals. Every figure starts from the scientific question, not from a template.

## Design Principles

**1. One figure, one core message.**
CNS reviewers skim fast. A figure must convey its main conclusion in 3 seconds. Remove gridlines, borders, and legend entries that dilute the core message. Default to minimal, not maximal.

**2. Restrained color > abundant color.**
Default palettes (matplotlib tab10, ggplot2 hue_pal, Excel colors) signal "not designed" instantly. Use 2-4 semantic main colors + 1 accent. Use the colourblind-safe `nature-default` theme unless the user selects a named alternative. The theme library, custom recoloring protocol, and preview gallery are defined in `references/color-palettes.md`.

For a requested refresh of the README 图表索引 thumbnails, use `scripts/recolor_figure_atlas.py` with a named library theme. This is a style-only transformation: preserve the original thumbnail geometry, labels, statistical annotations, and neutral ink; regenerate the palette gallery before updating the README.

**3. Design for print, not screen.**
Journal column widths are fixed (89 mm single, 183 mm double). Set figure dimensions at creation time — never scale down post-render. At final size, use Arial/Helvetica, 5-7 pt routine text, and 8 pt bold upright lowercase panel labels.

**4. Vector first, raster as fallback.**
Line art, scatter plots, bar charts → editable PDF/SVG/EPS. Only true raster content (heatmap colour blocks, micrographs) should use TIFF/PNG at ≥450 dpi. Keep the working colour space RGB.

---

## Complete Workflow

Follow this closed loop for every request. Never skip steps. Never assume the user's question.

```
User request received
       │
       ▼
  Step -1: Understand the Task ←── DISPATCH FIRST. If the user gave data but
       │                         didn't say what they want to learn, ASK.
       ▼
  Step 0: Parse Data, Match to Task ←── Data parsing is directed by the
       │                                question, not by a template.
       ▼
  Step 1: Recommend & Justify ←── "To answer your question, you need these
       │                         N panels. Here's why." N depends on the
       ▼                         question, not on a fixed number.
  User Confirms ──→ No → Refine recommendation
       │
       ▼ Yes
  Step 2: Runtime & Environment ←── Detect Python + R availability.
       │                            Install or configure if missing.
       ▼
  Step 3: Style Baseline Injection ←── typography + color + export blocks.
       │                               Copied VERBATIM into every script.
       ▼
  Step 4: Production Asset Scan ←── ls assets/figures/. For EVERY panel in
       │                            the plan, check matching scripts.
       ▼
  Step 5: Generate ←── COPY-FIRST for matching scripts → native run.
       │              No match → cross-type inherit.
       ▼
  Step 5.5: Validate Data ←── Data sanity checks BEFORE rendering.
       │
       ▼
  Step 6: QA Protocol ←── 4-pass QA (AP-0..AP-7, CL-1..CL-7,
       │                  VI-1..VI-6, VV-1..VV-6). Fix → re-render.
       ▼
  Step 6.5: Palette Personalization ←── Show the rendered preview, then offer
       │                                  a named theme, hex colours, or a
       │                                  reference palette image for recoloring.
       ▼
  Step 7: Deliver ←── Editable vector master + 450dpi RGB raster proof
                      + QA report + statistics report
```

---

### Step -1: Understand the Task — DISPATCH FIRST

**Before reading a single data file, understand what the user is trying to learn.** A dataset without a question is a spreadsheet, not a figure. The entire visualization plan flows from this question.

**图型选择规则：** 当用户不知道该画什么、要求补充图型、或需求属于专业场景（组学、生存、空间、网络、项目管理、业务监控）时，先读取 `references/figure-type-catalog.md`。按信息任务选择图型，并确认其状态是生产模板、图鉴模式还是按需实现；目录只负责选择与约束，不得把“图鉴模式”误报为已有可直接运行的生产脚本。

Classify the request into one of:

| User intent | Signal | Example |
|-----------|--------|---------|
| **User specified figure types** | "Make a volcano plot" / "画个热图" | User knows what they want. Proceed to Step 1 with the specified types. |
| **User has a question + data** | "Does Treatment affect Pheno1?" / "What drives Group differences?" | User has a scientific question. Proceed to Step 0. |
| **User gave data, no question** | "Analyze this data" / "Visualize this" / "看看这个数据" | **STOP. Ask the user: "What are you trying to learn from this data? Are you comparing groups? Looking for correlations? Finding outliers? Testing a hypothesis?"** Do NOT proceed until the user clarifies. Never generate generic "analysis" without a question. |
| **Cosmetic fix** | "Change this bar to blue" / "调整字号" | Skip to Steps 4-6. No contract needed. |

**If the user gave data without a question, the default response is a question, not a figure.**

---

### Step 0: Classify & Parse

**Step 0a — Classify the figure archetype FIRST.** Before parsing data, classify the figure into one of four archetypes. This determines layout strategy.

| Archetype | Description | Layout Strategy |
|-----------|------------|----------------|
| `quantitative_grid` | All panels carry equal scientific weight. Standard grid of related data plots. | **Symmetric.** No hero panel. Equal panel sizes. |
| `schematic-led` | A schematic/model diagram anchors the figure, supported by data panels. | **Asymmetric.** The schematic IS the hero. Data panels are supporting. |
| `image_plate + quant` | Microscopy/images paired with quantitative analysis. | **Asymmetric.** The image plate IS the hero. Quant panels are supporting. |
| `asymmetric_mixed` | Panels have different information density. One dense overview (heatmap/PCA/UMAP) dominates. | **Asymmetric.** The densest panel IS the hero. |

**If unsure, default to `asymmetric_mixed`** — it produces the Nature-style look of one dominant panel + subordinate evidence panels. Pure symmetric grids are rare in top-tier journals outside of supplement.

Pass the archetype to `compose_figure(archetype=...)`. The engine auto-detects which panel is the hero and applies asymmetric layout when the archetype is not `quantitative_grid` or `symmetric`.

**Step 0a.1 — Create the figure design brief for 2+ panels.** Before any panel code, read `references/figure-design-brief.md` and state the canvas ratio, core message, journal profile when named, hero panel, support sequence, and stable colour roles. Select one of its composition recipes; do not assemble a multi-panel figure as an unplanned grid. This brief is a required input to the later visual QA review.

For three or more benchmark metrics, method variants, or ablation blocks, explicitly evaluate the `benchmark-strip` recipe. Use a wide canvas only when it preserves readable labels and a left-to-right evidence sequence; reserve a legend-only cell when four or more series cannot be labeled directly or placed outside the data area.

**Step 0b — Parse data.** Once the archetype is classified, read and analyze the data — but only the aspects relevant to the question.

1. **Parse structure:** Load the data. Count rows, columns. Classify each column (continuous / categorical / group label / identifier).

**DATA INTEGRITY RULE — NON-NEGOTIABLE:**

- **Use ALL user-provided data.** Never downsample, never select "representative" rows, never pick "a few columns to keep it simple", never `np.random.choice(df, 12)` when the user gave 1200 rows. The user's data IS the ground truth. Reducing it is fabricating evidence.
- **If rendering performance is a concern** (e.g. scatter plot with >50K points), use `rasterized=True` or vector-friendly density representations. Never subsample to solve a rendering problem.
- **If a production script expects a different data shape** than the user provided (e.g. script needs `real_value.csv + pred_value.csv` but user has `Pheno1-Pheno8`), do NOT silently adapt by picking two columns. Inform the user: "This script expects paired X/Y data. Your data has N columns. Which two should I use as X and Y?" Wait for confirmation before proceeding.
- **If you drop any rows or columns for ANY reason**, state exactly how many were dropped, why, and get user acknowledgment in the QA report. Silent data loss is the #2 most serious bug in this skill.

2. **Run question-directed analysis:** The question determines what to compute.
   - "Does X differ between groups?" → Compute group means, between/within variance, pairwise tests
   - "What drives Y?" → Compute correlation matrix, PCA, feature importance
   - "Are these two variables related?" → Compute correlation, fit line, check residuals
   - "What's the distribution?" → Compute summary stats, test normality, detect outliers
3. **Do NOT run generic analysis.** If the question is about group differences, don't report the full correlation matrix. If the question is about correlation, don't compute group means for every possible partition. Data parsing serves the question, not the other way around.

---

### Step 1: Recommend Figures & Justify

Based on the question and the data morphology, propose a visualization plan. For each panel, state:

1. **What question does this panel answer?** — One sentence per panel.
2. **Why this figure type?** — Justify the choice based on data characteristics, not habit.
3. **How many panels?** — Determined by the number of distinct questions, not by a template. Two questions → two panels. Six questions → six panels. No filler panels.

The recommendation must follow this structure:

```
Visualization Plan

Scientific goal: [one sentence — what the user wants to learn]

| Panel | Figure type | Answers | Data basis |
|-------|------------|---------|------------|
| (a)   | [type]     | [question] | [e.g. Pheno1-6 all r>0.9 → heatmap] |
| (b)   | [type]     | [question] | [e.g. PC1=92% → PCA with group coloring] |
| ...   | ...        | ...     | ... |

Total: N panels. Layout: [M×N]. Journal: [target].
```

**Re-evaluate after user feedback.** If the user says "also show X" or "don't need Y", update the plan and re-present. Only proceed after explicit confirmation.

---

### Step 2: Runtime & Environment

After the plan is confirmed, before generating any code, verify the execution environment.

1. **Detect available runtimes:**

```bash
python --version 2>/dev/null || python3 --version 2>/dev/null
Rscript --version 2>/dev/null || ls "/c/Program Files/R/"*/bin/Rscript.exe 2>/dev/null
```

Store as `PYTHON_AVAILABLE`, `R_AVAILABLE`, `R_PATH`.

2. **Match runtimes to the plan:** For each panel in the confirmed plan:
   - If a production script exists (will be checked in Step 3) → the script's language must have a runtime
   - If no production script exists → generate in Python (default) or R (user preference)

3. **Handle missing runtimes:**
   - R panel requested but R not found → Tell user: "Panel (c) needs R with ComplexHeatmap. Install R or I'll use Python fallback (lower quality)."
   - Python panel requested but Python not found → Tell user: "Python not found. Install Python 3.9+."
   - Missing R packages → `install.packages(...)` command provided
   - Missing Python packages → `pip install ...` command provided

**Do not silently fall back.** The user decides whether to install the missing runtime or accept lower quality.

---

### Step 3: Style Baseline Injection (ALWAYS FIRST)

Load these four files and copy their "COPY VERBATIM" code blocks into the script — in order, at the very top, before any panel logic:

1. `references/typography.md` — rcParams/theme block. Fonts, spines, ticks, legend defaults.
2. `references/color-palettes.md` — PALETTE constants. All color variables.
3. `references/export-specs.md` — font embedding + save function.
4. `references/visual-style.md` — hierarchy, chart-specific mark rules, and final visual review.

**Palette selection is part of the style baseline.** Read the theme table in `references/color-palettes.md` before writing plotting code. Record the selected theme in the script header and map its colours to stable semantic roles (baseline, comparison, emphasis, context). If the user gives no preference, use `nature-default`; do not silently substitute matplotlib, seaborn, ggplot2, Excel, rainbow, or `tab10` colours.

**Journal-aware starting point:** if the user names a journal or target publication context, read `references/journal-intel.md` before selecting a theme. Use its routed theme only as the initial style baseline; a user-selected theme, hex set, or reference palette overrides it. Record the final choice as `routed` or `user override` in the script header and QA report. Journal styling must never alter data, statistics, panel order, or the semantic role of a comparison.

Also read `references/journal-specs.md` for target dimensions (89mm single / 183mm double).

For any two-or-more-panel figure, also apply `references/figure-design-brief.md` and `references/multipanel-layout.md`: aspect ratio and hierarchy are fixed before plotting, while `audit_figure` remains the non-negotiable export gate.

---

### Step 4: Production Asset Scan (EVERY panel)

**Run AFTER plan confirmation, BEFORE code generation. For EVERY panel in the confirmed plan:**

1. **First, read `references/figure-type-catalog.md` and `references/directory-map.md`.** The catalog selects the information task and records constraints; the directory map then maps user language (Chinese + English) to exact `assets/figures/<dir>/` paths. Find the user's description in the "Keywords" column → use the exact directory path. This prevents the #2 recurring bug: "柱状图" matching the wrong bar sub-directory.
2. Verify with `ls assets/figures/<matched-dir>/` that the directory exists and has scripts.
3. Check the matching directory for production scripts (`.py`, `.R`, `.r`).
4. For each match, check if the script's language runtime is available (from Step 2).
5. **Verify script can work with user data.** Read the script. Identify the script's "data entry points" — which variables receive external data (column names, data frames, file paths). Map them to the user's data columns. If the mapping exists but columns differ (e.g. script expects `length`/`number_of_cds` but user has `Pheno1`/`Pheno2`), mark as "visual adapt" — the script's visual system is preserved, only data mapping changes. Only mark as "incompatible" when the data STRUCTURE fundamentally differs (e.g. script expects paired X/Y CSV files but user has a single wide table).
6. **Fallback:** Only if `directory-map.md` has no matching entry, consult the catalog status, then scan `ls assets/figures/` and match directory names. For a catalog type marked `按需实现`, create a type-specific work script after confirming the data contract; do not silently substitute a different chart type.

Decision per panel:

```
Panel type matched in assets/figures/<type>/
    │
    ├── Script exists + runtime available + data STRUCTURE matches → COPY-FIRST.
    │   1. Copy the ENTIRE script file to work_dir/<panel>_production.<ext>
    │   2. Find the data-loading line, replace ONLY the data path
    │   3. Execute: subprocess.run([python/r_bin, script])
    │   4. If FAIL: log reason → downgrade to VISUAL ADAPT with notice
    │   5. If OK: load rendered PNG via Image.open() in composition
    │   Panel quality = PRODUCTION. NEVER write a drawing function for this panel.
    │
    ├── Script exists + data COLUMNS differ but STRUCTURE matches → VISUAL ADAPT (NEW).
    │   The script's visual system (layout, coords, colormap, annotations, inset
    │   positioning, statistical overlays) is PRESERVED. Only the data mapping changes.
    │
    │   VISUAL ADAPT protocol — PRESERVES production script's visual system:
    │
    │   **Step 0: SEMANTIC MATCH CHECK (NEW — run BEFORE column mapping).**
    │   Open the production script's companion PNG. Answer:
    │   - What does this script actually PRODUCE? (scatter with marginal density?
    │     grouped KDE? 2D kernel density contour? ridgeplot? violin?)
    │   - What does the USER want? (from their request: "边际密度图", "核密度图",
    │     "分布图", "density", "KDE", etc.)
    │   - Are they semantically compatible? (1D vs 1D? 2D vs 2D? same number of
    │     data dimensions?)
    │
    │   **If YES → Proceed to Step 1 (column mapping).**
    │   The script produces what the user wants. Column names differ but the
    │   visual system (layout, axes, transformations) can be preserved.
    │
    │   **If NO → STOP. Do not VISUAL ADAPT.**
    │   Column mapping cannot fix a semantic mismatch. A JointGrid 2D scatter
    │   script cannot produce a 1D marginal density plot no matter how you map
    │   columns. Two cases:
    │   - User wants 1D density of multiple variables → cross-type inherit from
    │     Ridge (density fill + bandwidth) or KDE/Density (distribution pattern)
    │   - User wants 2D scatter density → find a semantically matching 2D script
    │
    │   1. Identify the script's data entry points:
    │      - What column names does it reference? (e.g. "length", "number_of_cds")
    │      - What grouping variable? (e.g. "type", "Group")
    │      - What filtering columns? (e.g. "is_drep95")
    │   2. Map to user's data:
    │      - Script column X → User column ____ (choose most semantically similar)
    │      - Script column Y → User column ____
    │      - Script grouping col → User column ____ (or None if user has no groups)
    │   3. PRESENT THE MAPPING TO THE USER for confirmation.
    │   4. **Data range compatibility check (NEW):** Before copying the script, verify
    │      that the user's data values are compatible with the script's mathematical
    │      operations. Specifically check:
    │      - Does the script use log-scale axes? → User data must have NO values ≤ 0
    │      - Does the script normalize to [0,1]? → User data must have finite range
    │      - Does the script use sqrt/division? → User data must be non-negative
    │      - Does the script bin continuous data? → User data must have sufficient range
    │
    │      If ANY check fails, identify which visual elements must be adapted:
    │      - Log scale with negative values → drop log transform, keep linear axes
    │      - Normalization with zero range → skip normalization, use raw values
    │      - Division by zero risk → add epsilon guard
    │      Tell the user which transforms were dropped and why.
    │   5. Copy the script. Modify ONLY:
    │      - Column name references (search-replace old col name → user col name)
    │      - Grouping column mapping (or set group=None if none)
    │      - Mathematical transforms that conflict with data range (from step 4)
    │      - Data path
    │      - NEVER modify: layout structure, color palettes, annotation logic,
    │        figure dimensions, export parameters
    │   6. Execute the adapted script. Verify output PNG renders.
    │   7. If execution fails: log reason → downgrade to PARAM INHERIT with notice
    │   Panel quality = PRODUCTION VISUAL SYSTEM. The layout and aesthetics are
    │   from the production script; only the data source changed.
    │
    ├── Script exists + data STRUCTURE incompatible → CROSS-TYPE INHERIT + INFORM.
    │   Tell user: "[dir] has scripts but fundamentally different data structure.
    │   Using cross-type inheritance. Visual quality will be lower."
    │
    ├── Script exists + runtime NOT available → EXTRACT PARAMETERS.
    │   Read the script's FULL content. Open its companion PNG.
    │   Extract Class A/B/C parameters. Cross-type inherit.
    │   Inform user of the quality tradeoff.
    │
    └── No script exists → CROSS-TYPE INHERIT.
        Borrow from similar figure type in the borrowing table below.
```

**Borrowing table (no matching script):**

```
Requested type     Borrow from          What transfers
─────────────────────────────────────────────────────
RDA                PCA                  scatter point size, alpha, ellipse style
Radar              Bar                  color palette ratio, legend style
KDE / Density      Ridge                alpha fill, line color, bandwidth factor
UpSet              Confusion Matrix     fill color, edge color, font size
Single-cell traj.  PCA                  scatter point size, alpha, colormap
Forest             Bar                  line width, marker size, color logic
Sankey             (use own if exists)  node color palette, flow alpha
Heatmap            CorrHeatmap          colormap, colorbar settings
Correlation Scatter Scatter (basic)     point size, alpha, regression line style
```

#### Class A/B/C parameter extraction

**Class A — Hard Parameters (copy verbatim):** Color hex, alpha, line widths, marker sizes, bandwidth, density scale, spacing ratios.

**Class B — Scaling Parameters (preserve ratio):** Font sizes → scale proportionally to Academic Figure Skill 7pt base. Figure dimensions → scale to journal column width.

**Class C — Logic Parameters (copy behavior):** Legend on/off, grid on/off, spine visibility, statistical annotation format, frameon.

#### Preview PNG — HARD RULE

**You MUST open the companion PNG before finalizing parameters.** Find the PNG with the same basename as the script. Inspect it. Ask: *Do my extracted parameters reproduce this visual output?* If uncertain → re-read the script.

---

### Step 5: Generate Code

**Asset Confirmation Table — MUST be the first lines of the generated script.**

Before any import, before any baseline block, the generated script MUST start with this exact comment block:

```python
# Academic Figure Skill Asset Confirmation (verified against assets/figures/)
# (a) [figure type] → [asset path or "cross-type inherit"] → [native run | param inherit]
# (b) [figure type] → [asset path or "cross-type inherit"] → [native run | param inherit]
# ...
# RULE: "native run" = load pre-rendered PNG via Image.open().ax.imshow().
#       "param inherit" = drawing function below that copies Class A/B/C values.
#       If a panel says "native run" and you write a drawing function, you broke the contract.
```

**COPY-FIRST RULE — this is a MECHANICAL rule, not a judgment call.**

For EVERY panel marked "native run" in the Asset Confirmation Table:

1. **Copy the production script file to a working file.** Use `shutil.copy()` or shell `cp`. The filename must be `<panel_label>_production.<ext>`.
2. **Modify ONLY the data path.** Open the copied file, find the line that reads data (`pd.read_csv(...)`, `read.csv(...)`, `read.delim(...)`), and replace the path with the user's data path. Change NOTHING else.
3. **Execute the copied script.** Python: `subprocess.run([sys.executable, script])`. R: `subprocess.run([r_bin, script])`.
4. **Verify output.** Check that the output PNG/PDF file exists and is non-zero. If execution fails (syntax error, missing package, data mismatch), log the error, set that panel to "param inherit" in a REVISED Asset Confirmation Table comment, and proceed with cross-type inheritance instead. The failure reason MUST appear in the QA report.
5. **For R scripts:** ensure `png(type="cairo")` and `showtext_auto(FALSE)` before `png()` per `references/r-rendering.md`.

**What this means in the composition script:**
- "native run" panels → NO drawing function. The script loads the pre-rendered PNG via `Image.open()`.
- "param inherit" panels → drawing function with Class A/B/C values extracted from the named asset.
- If a native run FAILED → REVISED table shows the downgrade to "param inherit" and the reason.

**Forbidden patterns (these indicate the COPY-FIRST rule was violated):**
- A drawing function whose name matches a panel marked "native run" in the table.
- A drawing function that is a "simplified version" of a production script.
- Importing functions from a production script instead of executing the whole script.

Script structure:
```
1. Asset Confirmation Table (MANDATORY — the first lines)
2. Style baseline (verbatim from Step 3) — ONCE at top
3. Data section — ALL user data loaded here, NEVER downsampled
4. Production script execution (for "native run" panels) — subprocess calls
5. Panel functions — PNG loaders for "native run", drawing functions for "param inherit"
6. compose_figure() call — handles layout, spacing, labels, export
```

**Mixed Python+R:** R panels run first to PNG at spec-correct dimensions. Python engine loads them via `ax.imshow()`.

**R PNG rendering:** Follow the three mandatory rules in `references/r-rendering.md`. Never skip them — they prevent the #1 recurring R PNG quality bug.

---

### Step 5.5: Validate Data Before Rendering

Run chart-type checks on every panel's data array. Fix failures before rendering.

```
Volcano: (padj < 0.05).sum() ≥ 10 AND ≤ 80%
AUROC:   (tpr - fpr).max() ≥ 0.15
Heatmap: np.std(data, axis=1).mean() > 0.2
Bar:     abs(means.max() - means.min()) / means.max() > 0.05
Corr:    abs(corr_mat).max() (off-diag) ≥ 0.3
PCA/RDA: between_group_var / within_group_var > 1.0
Box/Violin: abs(medians.max() - medians.min()) / data_range > 0.1
```

Also predict 3 visual problems at the target panel width. Fix them before rendering.

---

### Step 6: QA Protocol

Execute the 4-pass QA protocol from `references/checklist.md`.

- **Pass 0:** Anti-pattern scan (AP-0 through AP-7) + revision case cross-reference (VI-7)
- **Pass 1:** Code-level compliance (CL-1 through CL-7)
- **Pass 2:** Visual logic & data integrity (VI-1 through VI-6)
- **Pass 3:** Rendered output verification (VV-1 through VV-5)

**Mandatory render gate:** before every `fig.savefig`, call `audit_figure(fig, figure_name)` from `scripts/visual_qa.py`. The gate renders the canvas and rejects (1) legends placed over an axes data area, (2) visible text outside the canvas, and (3) substantial text-to-text overlap. If it fails, move the legend outside the data area or use direct labels, adjust layout, then re-render and re-audit. A figure that fails this gate must never be exported or added to the README.

**Mandatory grayscale-proof gate:** after every final PNG proof is rendered, run `python scripts/grayscale_proof.py <preview.png> --output <preview-grayscale.png>` and inspect both files at intended display size. Critical categories must remain distinguishable without colour alone. When two groups merge in the grayscale proof, add a direct label, marker shape, line style, hatch, or unambiguous ordering; do not merely exchange two similar colours. Record the proof path in the QA report. This produces an auditable image proof, not an unsupported automatic claim that any palette is accessible.

**Composition review for multi-panel figures:** compare the rendered figure with the five-line design brief from `references/figure-design-brief.md`. Confirm the intended aspect ratio, hero/support visual hierarchy, panel reading order, whitespace for annotations, and one-to-one semantic colour roles. If any item fails, revise the layout or palette assignment, then re-run the mandatory render gate.

**Journal-profile review:** when a target journal was named, confirm that the recorded journal profile and selected theme match the final figure, any user override is documented, and the journal-specific style baseline has not turned into unsupported visual storytelling. A palette may support hierarchy but cannot imply significance, causal direction, or model superiority.

**Comparison-panel review:** for multi-metric or ablation figures, confirm that the aspect ratio is justified by the number of metrics, repeated labels are removed only when a shared legend/title preserves interpretation, and any dense legend occupies reserved whitespace or its own axes. Use a hatch or thin edge only when it is necessary for grayscale-safe distinction; it must never be decorative.

QA Gateway: READY (all pass) → Deliver. FIX (≤2) → Fix and re-run. ESCALATE (>2) → Reviewer Simulation Mode.

If Python/R runtime is unavailable, skip Pass 3 and warn the user.

---

### Step 6.5: Palette Personalization Pass

After the first rendered PNG proof passes QA and before final delivery, state the theme used and ask exactly once:

> 当前预览使用 **[theme name]**。你想保留它，还是提供喜欢的十六进制颜色、配色图或论文图作为参考，让我在不改变数据、统计、图型和颜色语义的前提下重新绘制个性化配色版本？

If the user chooses a library theme, recolor all panels with that theme and retain the same category-to-colour mapping across the full figure. If the user supplies hex colours, confirm their semantic ordering before applying them. If the user supplies a reference palette image, extract a concise palette, show the inferred swatches and semantic mapping, then recolor after confirmation. A custom palette never removes redundant markers, direct labels, line types, or ordering used for accessibility.

---

### Step 7: Deliver

Output:
1. Complete code block
2. QA self-check report
3. Editable vector PDF/SVG master + 450dpi RGB PNG/TIFF proof
4. **Statistics & Reproducibility Report** — for every quantitative panel:
   - n definition (what does each replicate represent?)
   - center statistic (mean? median?)
   - spread / interval (SD? SEM? 95% CI? — define which one was used)
   - statistical test name
   - multiple-comparison correction (if applicable)
   - source-data traceability (which file/column produced each data point)
   - For ML/model figures: train/validation/test split, number of seeds/folds, metric definition, baseline definition
5. Suggested next step

**The statistics report is not optional.** A figure without statistical documentation is not a publication-grade figure. Reviewers expect this information and will request it if missing.

---

## Reviewer Simulation Mode

If the user asks "will this pass review?":

> Role: You are a reviewer for [journal]. Review through 5 lenses:
> 1. Scientific clarity — main message in 3 seconds?
> 2. Visual hierarchy — most important element draws the eye?
> 3. Color & accessibility — print-safe, colorblind-friendly?
> 4. Typography & labeling — legible at print size?
> 5. Overall polish — anything making you "frown"?

Output: structured feedback with priority (must-fix vs. suggestion) and fix instructions.

---

## Anti-Pattern Recognition

Flag these immediately when reviewing user code:
- Default color palettes → offer semantic palette
- Four-sided borders → offer clean left/bottom spine
- Legend inside plot → offer outside/direct labeling
- Screenshot-only export → offer vector PDF
- Jet/rainbow colormap → offer perceptually uniform
- Bar chart without individual points (n < 10) → offer strip/swarm overlay
- Default font → offer Arial/Helvetica

---

## Figure Type Routing

All figure types routed through `assets/figures/<type>/`. Adding a new type = adding a directory with scripts. No registration needed.

## Eval & Quality Tracking

```bash
# Full asset audit — scripts, syntax, baseline compliance
py academic-figure-skill/scripts/eval_runner.py
py academic-figure-skill/scripts/eval_runner.py --type PCA

# Trigger accuracy benchmark — 40 prompts, F1/precision/recall
py academic-figure-skill/scripts/trigger_benchmark.py
py academic-figure-skill/scripts/trigger_benchmark.py --calibrate

# QA validator coverage — test each check against known-good/bad scripts
py academic-figure-skill/scripts/qa_coverage.py

# Reference integrity — directory-map, PANEL_ASPECT, SKILL.md cross-links
py academic-figure-skill/scripts/check_references.py
py academic-figure-skill/scripts/check_references.py --json

# E2E integration — automated A/B scenario scoring
py academic-figure-skill/scripts/e2e_runner.py
py academic-figure-skill/scripts/e2e_runner.py --scenario S1_pca
```

## Cross-Platform Adapters

Generate platform-specific adapter files for non-Claude-Code agents:
```bash
python academic-figure-skill/scripts/generate_adapters.py            # all platforms
python academic-figure-skill/scripts/generate_adapters.py --target cursor  # Cursor only
```

Generated adapters are in `install/`:
- `install/cursor/.cursorrules` → copy to your project root for Cursor
- `install/copilot/copilot-instructions.md` → copy to `.github/` for GitHub Copilot
- `install/codex/manifest.yaml` + `instructions.md` → copy to `~/.codex/skills/academic-figure-skill/` for Codex
- `install/claude-code/README.md` → already supported natively via `~/.claude/skills/`

---

## References

### Always Load

| File | Purpose |
|------|---------|
| `references/figure-contract.md` | Scientific claim, evidence chain, archetype, review risks |
| `references/nature-publication-style.md` | Nature-ready typography, colour, axes, decoration, and export contract |
| `references/color-palettes.md` | Theme selection and custom recoloring protocol |
| `references/palette-library.json` | Canonical machine-readable theme values |
| `references/typography.md` | Font setup |
| `references/journal-specs.md` | Dimension and spine setup |
| `references/export-specs.md` | Format and resolution |
| `references/checklist.md` | Full QA checklist |

### On-Demand

| File | When |
|------|------|
| `references/journal-intel.md` | User specifies a target journal |
| `references/common-pitfalls.md` | After code generation |
| `references/revision-cases.md` | Figure type matches known case / "will this pass review" |
| `references/multipanel-layout.md` | Multi-panel figures — anti-redundancy, hero panel, narrative |
| `references/figure-design-brief.md` | Multi-panel figures — aspect ratio, composition recipes, colour roles, and pre-export hierarchy review |
| `references/directory-map.md` | Step 4 — maps user language to exact figure directory paths |
| `references/figure-type-catalog.md` | 图型选择不明确、要扩展图型、或属于专业 / 工作可视化场景 |
| `references/figure-deconstruction.md` | Compositional inspiration |
| `references/matplotlib.md` | Python/matplotlib/seaborn |
| `references/complexheatmap.md` | R heatmaps |
| `references/r-rendering.md` | R PNG output — cairo device, showtext off, spec-correct dimensions |

### Production Assets

| Path | When |
|------|------|
| `assets/figures/<type>/` | Step 4 — production script scan |
| `assets/figures/other/` | Long-tail fallback |
