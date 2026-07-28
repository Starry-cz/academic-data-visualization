#!/usr/bin/env python3
"""Academic Figure Skill Trigger Accuracy Benchmark.

Simulates Claude's skill dispatcher by scoring prompts against the SKILL.md
description field. Reports precision / recall / F1 / false-positive and
false-negative rates with misclassification analysis.

Test cases include the original boundary set plus two positive prompts for each
of the 24 registry categories.

Usage:
    py trigger_benchmark.py              # full benchmark
    py trigger_benchmark.py --json       # machine-readable output
    py trigger_benchmark.py --verbose    # show per-prompt scores
"""

from __future__ import annotations
import json, re, sys
from pathlib import Path

# 始终以当前脚本所在仓库为准，避免仓库改名后基准测试失效。
PROJECT = Path(__file__).resolve().parents[1]
SKILL_MD = PROJECT / "SKILL.md"

# ═══════════════════════════════════════════════════════════
# Test prompts — 40 cases
# ═══════════════════════════════════════════════════════════

SHOULD_TRIGGER = [
    # --- Direct figure type requests ---
    ("T01_pca_cn",       "帮我画一个PCA分析图"),
    ("T02_volcano_en",   "make a volcano plot from this DESeq2 output"),
    ("T03_heatmap_cn",   "绘制热图"),
    ("T04_journal_style","画一个Nature风格的火山图"),
    ("T05_multipanel",   "compose these 4 panels into a Nature-style figure"),
    ("T06_expr_heatmap", "visualize this expression matrix as a heatmap"),
    ("T07_review",       "review this figure for Nature Genetics submission"),
    ("T08_export_dpi",   "export this figure at 300dpi for manuscript submission"),
    ("T09_corr_heatmap", "draw a correlation heatmap of these variables"),
    ("T10_marginal_cn",  "画一个边际散点密度图"),
    # --- Scientific visualization intent ---
    ("T11_violin_cn",    "帮我做一个小提琴图看组间差异"),
    ("T12_bar_group",    "comparing treatment groups with a grouped bar chart"),
    ("T13_ridge_cn",     "用山脊图展示多个基因在不同组织的表达分布"),
    ("T14_dotplot_en",   "make a marker gene dot plot from this single-cell data"),
    ("T15_sankey_cn",    "画桑基图展示细胞分化流向"),
    # --- Journal / publication intent ---
    ("T16_submit_nat",   "prepare this figure for Nature Communications submission"),
    ("T17_cell_style",   "make this look like a Cell Press figure"),
    ("T18_sci_format",   "format this plot for Science Advances"),
    # --- Polish / review ---
    ("T19_polish_fig",   "polish this figure — it looks amateur"),
    ("T20_vector_export","save this as vector PDF with embedded fonts for the journal"),
    # --- Two routing prompts for each of the 24 registry categories ---
    ("C01a_compare_cn", "画点图比较不同学校的平均得分和置信区间"),
    ("C01b_rank_en", "make a lollipop chart ranking the treatment effects"),
    ("C02a_time_cn", "绘制时间序列折线图并显示置信带"),
    ("C02b_gantt_en", "make a Gantt chart for the longitudinal study schedule"),
    ("C03a_dist_cn", "画ECDF图比较三组数据分布"),
    ("C03b_qq_en", "create a Q-Q plot to inspect residual normality"),
    ("C04a_reg_cn", "画回归散点图展示剂量反应关系"),
    ("C04b_agree_en", "make a Bland-Altman plot for method agreement"),
    ("C05a_dim_cn", "画UMAP图展示样本的低维结构"),
    ("C05b_parallel_en", "create a parallel coordinates plot for these multivariate profiles"),
    ("C06a_matrix_cn", "绘制带分组注释的聚类热图"),
    ("C06b_calendar_en", "make a calendar heatmap of daily measurements"),
    ("C07a_effect_cn", "画森林图展示效应量和95%置信区间"),
    ("C07b_coef_en", "create a coefficient plot with confidence intervals"),
    ("C08a_pr_cn", "绘制PR曲线和校准曲线评估分类模型"),
    ("C08b_resid_en", "make a residual diagnostic plot for this regression model"),
    ("C09a_shap_cn", "画SHAP蜂群图解释模型预测"),
    ("C09b_pdp_en", "create a partial dependence plot for the top features"),
    ("C10a_comp_cn", "画百分比堆叠柱状图展示组成"),
    ("C10b_likert_en", "make a diverging stacked bar chart for Likert responses"),
    ("C11a_set_cn", "画UpSet图展示六个集合的交集"),
    ("C11b_euler_en", "create an Euler diagram for these overlapping sets"),
    ("C12a_flow_cn", "绘制CONSORT流程图说明受试者纳排"),
    ("C12b_alluvial_en", "make an alluvial diagram for stage transitions"),
    ("C13a_network_cn", "画共现网络展示节点社区和边权"),
    ("C13b_arc_en", "create an arc diagram for this weighted graph"),
    ("C14a_map_cn", "画分级设色地图展示各省标准化率"),
    ("C14b_flowmap_en", "make a flow map from these origin-destination coordinates"),
    ("C15a_survival_cn", "绘制Kaplan-Meier生存曲线和风险表"),
    ("C15b_swimmer_en", "make a swimmer plot for treatment duration and events"),
    ("C16a_love_cn", "画Love Plot检查倾向评分匹配后的协变量平衡"),
    ("C16b_dca_en", "create a decision curve figure for the clinical model"),
    ("C17a_gwas_cn", "画曼哈顿图展示GWAS关联信号"),
    ("C17b_gsea_en", "make a GSEA enrichment curve from this ranked gene list"),
    ("C18a_singlecell_cn", "绘制单细胞UMAP和标记基因点图"),
    ("C18b_spatial_en", "make a spatial transcriptomics feature plot over the tissue coordinates"),
    ("C19a_micro_cn", "把显微图像板和样本级定量图组合成论文图"),
    ("C19b_line_en", "create a line-scan intensity plot for these microscopy channels"),
    ("C20a_irt_cn", "画题目特征曲线和测验信息曲线"),
    ("C20b_sem_en", "make an SEM path figure with standardized coefficients"),
    ("C21a_did_cn", "绘制双重差分图检查政策实施前后的趋势"),
    ("C21b_rdd_en", "create a regression discontinuity plot around the cutoff"),
    ("C22a_cocite_cn", "画共被引网络展示知识结构"),
    ("C22b_burst_en", "make a keyword burst plot for this bibliometric dataset"),
    ("C23a_qc_cn", "绘制控制图监测批次质量是否稳定"),
    ("C23b_retention_en", "make a cohort retention heatmap for the study workflow"),
    ("C24a_composite_cn", "把图像、统计结果和流程图排成非对称多面板论文图"),
    ("C24b_small_en", "compose a small-multiples figure with consistent axes and labels"),
]

SHOULD_NOT_TRIGGER = [
    # --- Statistical analysis without viz intent ---
    ("F01_t_test",       "帮我看看这组数据统计显著性"),
    ("F02_p_value",      "calculate p-values for these groups and report"),
    ("F03_anova",        "run a two-way ANOVA on this dataset"),
    # --- Data cleaning ---
    ("F04_clean_csv",    "clean up this CSV file and remove outliers"),
    ("F05_normalize",    "normalize this count matrix to TPM"),
    # --- Writing tasks ---
    ("F06_results_sec",  "write the results section for my RNA-seq paper"),
    ("F07_abstract",     "draft an abstract for this manuscript"),
    # --- Code / debugging ---
    ("F08_index_error",  "fix this indexing error: IndexError on line 47"),
    ("F09_import_fix",   "why is my matplotlib import failing?"),
    # --- Literature / reading ---
    ("F10_literature",   "summarize the latest papers on CRISPR editing"),
    ("F11_find_paper",   "find papers that used UMAP for microbiome data"),
    # --- Charts excluded by design ---
    ("F12_pie_chart",    "make a pie chart showing my budget allocation"),
    ("F13_3d_chart",     "create a 3D rotating chart of this data"),
    # --- Presentation / dashboard ---
    ("F14_ppt_slide",    "create a presentation slide summarizing these results"),
    ("F15_dashboard",    "plot a sales trend dashboard in PowerBI"),
    ("F16_plotly",       "make an interactive plotly scatter for my website"),
    # --- Photo / image editing ---
    ("F17_photo_edit",   "enhance this microscopy image contrast"),
    ("F18_image_crop",   "crop and resize these Western blot images"),
    # --- Math function plots ---
    ("F19_math_plot",    "plot the function f(x) = sin(x)/x"),
    ("F20_3d_surface",   "plot z = x^2 + y^2 as a 3D surface"),
]

# ═══════════════════════════════════════════════════════════
# Skill description matching simulation
# ═══════════════════════════════════════════════════════════

def _load_description() -> str:
    """Extract the description field from SKILL.md frontmatter."""
    text = SKILL_MD.read_text(encoding="utf-8")
    m = re.search(r'description:\s*(.+?)(?:\n\w+:|$)', text, re.DOTALL)
    if not m:
        return ""
    return m.group(1).strip()


# Signal words derived from SKILL.md description + body
TRIGGER_SIGNALS = [
    # Strong (score += 3): exact figure type mentions (English — \b boundaries)
    (3, [
        r"\b(?:volcano|heatmap|boxplot|scatter|bar\s*chart|violin|ridge|sankey|pca|umap|t-sne|auroc|roc|upset|radar|kde|dot\s*plot|forest\s*plot|manhattan|qq)\b",
        r"\bcorrelation\s+(?:matrix|heatmap)\b",
        r"\b(?:marginal|grouped|stacked)\s+(?:density|bar|violin)\b",
        r"\bmarker\s+gene\b",
    ]),
    # Strong (score += 3): Chinese figure type mentions (no \b — Chinese chars)
    (3, [
        "热图", "火山图", "散点图", "箱线图", "柱状图", "小提琴图",
        "雷达图", "山脊图", "桑基图", "边际", "核密度", "密度图",
        "相关矩阵", "点图", "气泡图", "森林图", "小提琴",
        "PCA分析", "主成分分析",
    ]),
    # Medium (score += 2): figure/plot/chart intent (English)
    (2, [
        r"\b(?:figure|plot|chart|graph|panel)s?\b",
        r"\b(?:make|create|draw)\b.*\b(?:diagram|map|curve)s?\b",
        r"\bcompose\b.*\b(?:panel|figure|plot)\b",
        r"\bmulti.panel\b",
        r"\bvisuali[sz]e\b.*\b(?:as|with|in)\b.*\b(?:figure|plot|chart|heatmap)\b",
    ]),
    # Medium (score += 2): Chinese drawing intent
    (2, [
        "画", "绘制", "作图", "绘图", "画图", "可视化", "做.*图", "论文图", "多面板",
    ]),
    # Weak (score += 1): journal / publication context
    (1, [
        r"\b(?:Nature|Cell|Science)\b.*\b(?:figure|plot|style|format|journal)\b",
        r"\bmanuscript\b.*\bsubmission\b",
        r"\bpublication\b.*\b(?:ready|grade|quality)\b",
        r"\b(?:polish|review|export|save|format)\b.*\b(?:figure|plot|as)\b",
        r"\b300dpi\b|\bvector\s*(?:PDF|export)\b|\bcairo_pdf\b",
        r"\bembedded\s+fonts\b",
    ]),
]

# Exclusion signals — any match → score = 0 regardless of trigger signals
EXCLUSION_SIGNALS = [
    # Excluded chart types
    r"\bpie\s*chart\b",
    r"(?i)\b3D\s*(?:chart|plot|rotating|surface)\b",
    r"\bdonut\s*chart\b",
    # Dashboard / interactive
    r"\b(?:dashboard|PowerBI|Tableau)\b",
    r"(?i)\b(?:Plotly|Bokeh|Altair)\b",
    r"\binteractive\b.*\b(?:plot|chart|dashboard)\b",
    # Presentation / document
    r"\b(?:PowerPoint|presentation|slide\s*deck)\b",
    r"\bcreate\s+a\s+slide\b",
    # Data analysis without viz intent
    r"\b(?:calculate|compute|run)\b.*\b(?:p.value|t.test|ANOVA|significance|statistical)\b",
    r"\bstatistical\s+(?:test|significance|analysis)\b(?!.*\b(?:plot|figure|visualize|chart)\b)",
    # Data cleaning / processing
    r"\b(?:clean|normalize|impute|remove\s*outliers)\b.*\b(?:data|CSV|matrix|file)\b",
    r"\bnormalize\b.*\b(?:count|matrix|TPM|FPKM)\b",
    # Writing tasks
    r"\b(?:write|draft)\b.*\b(?:results|abstract|manuscript|paper|section)\b",
    # Code debugging
    r"\b(?:debug|fix|error|bug|why\s+is|how\s+do\s+I\s+fix)\b",
    r"\bimport\s+fail",
    # Literature review / paper finding
    r"\b(?:summarize|review|find)\b.*\b(?:paper|article|literature|latest)\b",
    r"\bfind\s+papers\b",
    # Photo / image editing
    r"\b(?:enhance|crop|resize|brightness|contrast)\b.*\b(?:image|photo|microscopy|blot)\b",
    # Pure math function plots
    r"\bplot\s+the\s+function\b",
    r"\bf\([xyz]\)\s*=",
    r"\bz\s*=\s*x\^2",
    # Illustrator / Figma
    r"\b(?:Illustrator|Figma|Photoshop|InDesign)\b",
]


def score_prompt(prompt: str) -> int:
    """Score a prompt: 0 = should NOT trigger, >0 = should trigger (higher = stronger).

    Returns 0 if any exclusion signal matches. Otherwise returns the sum of
    weighted trigger signals.
    """
    prompt_lower = prompt.lower()

    # Exclusion: any match → do not trigger
    for pattern in EXCLUSION_SIGNALS:
        if re.search(pattern, prompt_lower):
            return 0

    # Trigger signals: weighted sum
    score = 0
    for weight, patterns in TRIGGER_SIGNALS:
        for pattern in patterns:
            if re.search(pattern, prompt_lower):
                score += weight

    return score


def classify(score: int, threshold: int = 2) -> bool:
    """Scores >= threshold → trigger."""
    return score >= threshold


# ═══════════════════════════════════════════════════════════
# Benchmark runner
# ═══════════════════════════════════════════════════════════

def run_benchmark(threshold: int = 2) -> dict:
    prompt_scores = []

    for tid, prompt in SHOULD_TRIGGER:
        s = score_prompt(prompt)
        triggered = s >= threshold
        prompt_scores.append({
            "id": tid, "prompt": prompt, "should_trigger": True,
            "score": s, "triggered": triggered, "correct": triggered,
        })

    for fid, prompt in SHOULD_NOT_TRIGGER:
        s = score_prompt(prompt)
        triggered = s >= threshold
        prompt_scores.append({
            "id": fid, "prompt": prompt, "should_trigger": False,
            "score": s, "triggered": triggered, "correct": not triggered,
        })

    tp = sum(1 for p in prompt_scores if p["should_trigger"] and p["triggered"])
    tn = sum(1 for p in prompt_scores if not p["should_trigger"] and not p["triggered"])
    fp = sum(1 for p in prompt_scores if not p["should_trigger"] and p["triggered"])
    fn = sum(1 for p in prompt_scores if p["should_trigger"] and not p["triggered"])

    total = len(prompt_scores)
    accuracy = (tp + tn) / total if total > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    fp_cases = [p for p in prompt_scores if not p["should_trigger"] and p["triggered"]]
    fn_cases = [p for p in prompt_scores if p["should_trigger"] and not p["triggered"]]

    return {
        "threshold": threshold,
        "total": total,
        "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "accuracy": round(accuracy, 3),
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3),
        "false_positives": fp_cases,
        "false_negatives": fn_cases,
        "all_scores": prompt_scores,
    }


def calibrate_threshold() -> dict:
    """Sweep thresholds 1-6 and return the best F1."""
    best = None
    for t in range(1, 7):
        r = run_benchmark(t)
        if best is None or r["f1"] > best["f1"]:
            best = r
    return best


if __name__ == "__main__":
    verbose = "--verbose" in sys.argv
    use_json = "--json" in sys.argv
    calibrate = "--calibrate" in sys.argv

    if calibrate:
        result = calibrate_threshold()
    else:
        result = run_benchmark(threshold=2)

    if use_json:
        print(json.dumps({
            k: v for k, v in result.items() if k != "all_scores"
        }, indent=2, ensure_ascii=False))
        sys.exit(0)

    print("=" * 64)
    print("Academic Figure Skill Trigger Accuracy Benchmark")
    print(f"Skill: {_load_description()[:80]}...")
    print("=" * 64)
    print(f"Threshold: score >= {result['threshold']}")
    print(
        f"Total prompts: {result['total']} "
        f"({len(SHOULD_TRIGGER)} should-trigger + {len(SHOULD_NOT_TRIGGER)} should-not)"
    )
    print()
    print(f"  True Positives  : {result['tp']:2d}  (should trigger, did)")
    print(f"  True Negatives  : {result['tn']:2d}  (should NOT trigger, didn't)")
    print(f"  False Positives : {result['fp']:2d}  (should NOT, DID — over-trigger)")
    print(f"  False Negatives : {result['fn']:2d}  (should, didn't — missed)")
    print()
    print(f"  Accuracy :  {result['accuracy']:.0%}")
    print(f"  Precision:  {result['precision']:.0%}")
    print(f"  Recall   :  {result['recall']:.0%}")
    print(f"  F1 Score :  {result['f1']:.0%}")
    print()

    # Misclassification analysis
    fps = result["false_positives"]
    fns = result["false_negatives"]

    if fps:
        print(f"--- FALSE POSITIVES ({len(fps)}) — over-triggered, add exclusion ---")
        for p in fps:
            print(f"  [{p['id']}] score={p['score']}: \"{p['prompt'][:90]}\"")

    if fns:
        print(f"--- FALSE NEGATIVES ({len(fns)}) — missed, add trigger signal ---")
        for p in fns:
            print(f"  [{p['id']}] score={p['score']}: \"{p['prompt'][:90]}\"")

    if not fps and not fns:
        print(f"All {result['total']} prompts correctly classified.")

    print("=" * 64)
    if result["f1"] >= 0.95:
        print("Verdict: EXCELLENT — trigger accuracy is production-grade")
    elif result["f1"] >= 0.85:
        print("Verdict: GOOD — minor tuning needed")
    elif result["f1"] >= 0.70:
        print("Verdict: ADEQUATE — review misclassifications above")
    else:
        print("Verdict: NEEDS WORK — significant misclassification rate")

    if verbose and result.get("all_scores"):
        print()
        print("--- Per-prompt scores ---")
        for p in result["all_scores"]:
            tag = "TRIGGER" if p["triggered"] else "skip"
            expected = "EXPECTED" if p["correct"] else "WRONG"
            print(f"  [{tag:7}] [{expected:8}] score={p['score']:2d}  {p['id']:20s}  \"{p['prompt'][:80]}\"")
