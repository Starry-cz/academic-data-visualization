#!/usr/bin/env python3
"""Render the verified, data-contract-first template set through one safe CLI."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch, Rectangle
from PIL import Image

from manifest_lib import sha256_file
from palette_lib import THEMES, THEME_IDS, resolve_theme


VERIFIER_VERSION = "2.0.0"
PROFILES = {
    "journal_print": {"figsize": (7.2047, 4.8), "dpi": 450, "font_size": 7.0},
    "report_web": {"figsize": (10.0, 6.0), "dpi": 200, "font_size": 11.0},
    "keynote_screen": {"figsize": (13.333333, 7.5), "dpi": 144, "font_size": 18.0},
    "poster_large": {"figsize": (12.0, 8.0), "dpi": 300, "font_size": 14.0},
}


@dataclass(frozen=True)
class Theme:
    """Approved semantic colour roles for one named repository theme."""

    theme_id: str
    categorical: tuple[str, ...]
    sequential: tuple[str, ...]
    diverging: tuple[str, ...]
    accent: str

    def __getitem__(self, index: int) -> str:
        return self.categorical[index]

    def __len__(self) -> int:
        return len(self.categorical)
MINIMUM_ROWS = {
    "grouped-bar-chart": 12,
    "line-chart": 12,
    "violin-plot": 12,
    "correlation-matrix": 10,
    "pca-biplot": 10,
    "forest-plot": 6,
    "roc-curve": 20,
    "precision-recall-curve": 20,
    "calibration-curve": 50,
    "volcano-plot": 20,
    "kaplan-meier-curve": 20,
    "sankey-diagram": 6,
}


def select_font(requested: str | None) -> str:
    """只使用明确批准且真实存在的字体，不静默接受任意替代字体。"""
    candidates = [requested] if requested else ["Arial", "Liberation Sans"]
    for family in candidates:
        if not family:
            continue
        try:
            font_manager.findfont(family, fallback_to_default=False)
            return family
        except ValueError:
            continue
    raise RuntimeError(
        "No approved sans-serif font is installed. Install Arial or Liberation Sans, "
        "or pass --font-family with an available journal-approved font."
    )


def configure_style(profile: str, theme_id: str, font_family: str) -> Theme:
    profile_spec = PROFILES[profile]
    registered = THEMES[theme_id]
    plt.rcParams.update(
        {
            "font.family": font_family,
            "font.size": profile_spec["font_size"],
            "axes.labelsize": profile_spec["font_size"],
            "axes.titlesize": profile_spec["font_size"] + 1,
            "xtick.labelsize": profile_spec["font_size"] - 0.5,
            "ytick.labelsize": profile_spec["font_size"] - 0.5,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.7,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.width": 0.7,
            "ytick.major.width": 0.7,
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
            "savefig.facecolor": "white",
            "figure.facecolor": "white",
        }
    )
    return Theme(
        theme_id=theme_id,
        categorical=tuple(registered["categorical"]),
        sequential=tuple(registered["sequential"]),
        diverging=tuple(registered["diverging"]),
        accent=str(registered["accent"]),
    )


def demo_data(chart_id: str, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    if chart_id == "grouped-bar-chart":
        rows = []
        for condition, offset in [("Control", 0.0), ("Treatment A", 0.7), ("Treatment B", 1.25)]:
            for group, base in [("Cohort 1", 1.4), ("Cohort 2", 2.1), ("Cohort 3", 2.8)]:
                for value in base + offset + rng.normal(0, 0.28, 14):
                    rows.append((group, condition, value))
        return pd.DataFrame(rows, columns=["group", "condition", "value"])
    if chart_id == "line-chart":
        rows = []
        for group, shift in [("Control", 0.0), ("Treatment A", 0.4), ("Treatment B", 0.8)]:
            for x in range(8):
                for value in 1.1 + shift + 0.22 * x + rng.normal(0, 0.22, 12):
                    rows.append((x, group, value))
        return pd.DataFrame(rows, columns=["x", "group", "value"])
    if chart_id == "violin-plot":
        rows = []
        for group, mean in [("Control", 0.0), ("Dose 1", 0.7), ("Dose 2", 1.35), ("Dose 3", 1.0)]:
            for value in rng.normal(mean, 0.55, 35):
                rows.append((group, value))
        return pd.DataFrame(rows, columns=["group", "value"])
    if chart_id == "correlation-matrix":
        latent = rng.normal(size=60)
        return pd.DataFrame(
            {
                "marker_a": latent + rng.normal(0, 0.35, 60),
                "marker_b": 0.8 * latent + rng.normal(0, 0.45, 60),
                "marker_c": -0.55 * latent + rng.normal(0, 0.55, 60),
                "marker_d": rng.normal(size=60),
                "marker_e": 0.35 * latent + rng.normal(0, 0.7, 60),
            }
        )
    if chart_id == "pca-biplot":
        rows = []
        for group, shift in [("Group A", -1.2), ("Group B", 0.2), ("Group C", 1.4)]:
            for index in range(22):
                f1 = rng.normal(shift, 0.7)
                f2 = rng.normal(-0.5 * shift, 0.65)
                rows.append((f"{group[-1]}{index + 1:02d}", group, f1, f2, f1 + f2 + rng.normal(0, 0.4), f1 - f2 + rng.normal(0, 0.35)))
        return pd.DataFrame(rows, columns=["sample_id", "group", "feature_1", "feature_2", "feature_3", "feature_4"])
    if chart_id == "forest-plot":
        estimate = np.array([-0.24, 0.31, 0.52, -0.08, 0.73, 0.18])
        half = np.array([0.22, 0.18, 0.25, 0.16, 0.28, 0.20])
        return pd.DataFrame({"label": [f"Outcome {c}" for c in "ABCDEF"], "estimate": estimate, "lower": estimate - half, "upper": estimate + half})
    if chart_id in {"roc-curve", "precision-recall-curve", "calibration-curve"}:
        y_true = rng.integers(0, 2, 180)
        score = np.clip(0.18 + 0.62 * y_true + rng.normal(0, 0.22, 180), 0, 1)
        return pd.DataFrame({"y_true": y_true, "score": score})
    if chart_id == "volcano-plot":
        log2fc = rng.normal(0, 1.15, 260)
        signal = np.abs(log2fc) + rng.gamma(1.1, 0.55, 260)
        p_value = np.clip(10 ** (-signal), 1e-8, 1)
        return pd.DataFrame({"feature": [f"Gene{i + 1}" for i in range(260)], "log2fc": log2fc, "p_value": p_value})
    if chart_id == "kaplan-meier-curve":
        rows = []
        for group, scale in [("Control", 18.0), ("Treatment", 27.0)]:
            event_time = rng.exponential(scale, 70)
            censor_time = rng.uniform(8, 42, 70)
            observed = event_time <= censor_time
            for time, event in zip(np.minimum(event_time, censor_time), observed, strict=True):
                rows.append((time, int(event), group))
        return pd.DataFrame(rows, columns=["time", "event", "group"])
    if chart_id == "sankey-diagram":
        return pd.DataFrame(
            {
                "source": ["Discovery", "Discovery", "Validation", "Validation", "Deployment", "Deployment"],
                "target": ["Selected", "Excluded", "Confirmed", "Rejected", "Adopted", "Deferred"],
                "value": [72, 28, 51, 21, 39, 12],
            }
        )
    raise ValueError(f"Unsupported verified chart: {chart_id}")


def require_columns(data: pd.DataFrame, names: list[str]) -> None:
    missing = [name for name in names if name not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_data(chart_id: str, data: pd.DataFrame) -> None:
    contracts = {
        "grouped-bar-chart": ["group", "condition", "value"],
        "line-chart": ["x", "group", "value"],
        "violin-plot": ["group", "value"],
        "forest-plot": ["label", "estimate", "lower", "upper"],
        "roc-curve": ["y_true", "score"],
        "precision-recall-curve": ["y_true", "score"],
        "calibration-curve": ["y_true", "score"],
        "volcano-plot": ["feature", "log2fc", "p_value"],
        "kaplan-meier-curve": ["time", "event", "group"],
        "sankey-diagram": ["source", "target", "value"],
    }
    if chart_id == "correlation-matrix":
        numeric = data.select_dtypes(include="number")
        if numeric.shape[1] < 3:
            raise ValueError("Correlation matrix requires at least three numeric columns")
    elif chart_id == "pca-biplot":
        require_columns(data, ["sample_id", "group"])
        if data.drop(columns=["sample_id", "group"]).select_dtypes(include="number").shape[1] < 3:
            raise ValueError("PCA biplot requires at least three numeric feature columns")
    else:
        require_columns(data, contracts[chart_id])
    minimum_rows = MINIMUM_ROWS[chart_id]
    if len(data) < minimum_rows:
        raise ValueError(f"{chart_id} requires at least {minimum_rows} observations/rows")
    if data.isna().any().any():
        raise ValueError("Missing values are not accepted; declare and handle them before plotting")
    if chart_id in {"roc-curve", "precision-recall-curve", "calibration-curve"}:
        if set(data["y_true"].unique()) - {0, 1}:
            raise ValueError("y_true must contain only 0 and 1")
        if data["y_true"].nunique() != 2:
            raise ValueError("y_true must contain both outcome classes")
        if not data["score"].between(0, 1).all():
            raise ValueError("score must lie in [0, 1]")
    if chart_id == "forest-plot" and not ((data["lower"] <= data["estimate"]) & (data["estimate"] <= data["upper"])).all():
        raise ValueError("Forest intervals must satisfy lower <= estimate <= upper")
    if chart_id == "volcano-plot" and not data["p_value"].between(0, 1, inclusive="right").all():
        raise ValueError("p_value must lie in (0, 1]")
    if chart_id == "sankey-diagram" and (data["value"] <= 0).any():
        raise ValueError("Sankey values must be positive")
    numeric_columns = {
        "grouped-bar-chart": ["value"],
        "line-chart": ["x", "value"],
        "violin-plot": ["value"],
        "forest-plot": ["estimate", "lower", "upper"],
        "roc-curve": ["y_true", "score"],
        "precision-recall-curve": ["y_true", "score"],
        "calibration-curve": ["y_true", "score"],
        "volcano-plot": ["log2fc", "p_value"],
        "kaplan-meier-curve": ["time", "event"],
        "sankey-diagram": ["value"],
    }.get(chart_id, [])
    invalid_numeric = [column for column in numeric_columns if not pd.api.types.is_numeric_dtype(data[column])]
    if invalid_numeric:
        raise ValueError(f"Columns must be numeric: {invalid_numeric}")
    if chart_id == "grouped-bar-chart" and (data.groupby(["group", "condition"]).size() < 2).any():
        raise ValueError("Each group-condition cell needs at least two observations")
    if chart_id == "line-chart" and (data.groupby(["group", "x"]).size() < 2).any():
        raise ValueError("Each group-x cell needs at least two observations for uncertainty")
    if chart_id == "kaplan-meier-curve":
        if set(data["event"].unique()) - {0, 1} or (data["time"] < 0).any():
            raise ValueError("Kaplan-Meier data require non-negative time and binary event")
        if (data.groupby("group")["event"].sum() == 0).any():
            raise ValueError("Each Kaplan-Meier group needs at least one observed event")
    if chart_id == "correlation-matrix":
        numeric = data.select_dtypes(include="number")
        if (numeric.std(ddof=1) == 0).any():
            raise ValueError("Correlation variables must have non-zero variance")
    if chart_id == "pca-biplot":
        features = data.drop(columns=["sample_id", "group"]).select_dtypes(include="number")
        if (features.std(ddof=1) == 0).any():
            raise ValueError("PCA feature columns must have non-zero variance")


def mean_ci(values: pd.Series) -> tuple[float, float]:
    array = values.to_numpy(dtype=float)
    return float(array.mean()), float(1.96 * array.std(ddof=1) / math.sqrt(len(array)))


def render_grouped_bar(data: pd.DataFrame, ax: plt.Axes, colors: Theme, rng: np.random.Generator) -> dict[str, Any]:
    groups = list(dict.fromkeys(data["group"].astype(str)))
    conditions = list(dict.fromkeys(data["condition"].astype(str)))
    width = 0.72 / len(conditions)
    metrics: dict[str, Any] = {"means": {}}
    hatches = ["", "///", "xx", "..", "\\\\", "++"]
    for index, condition in enumerate(conditions):
        positions = np.arange(len(groups)) - 0.36 + width / 2 + index * width
        means, cis = [], []
        for group in groups:
            subset = data[(data["group"].astype(str) == group) & (data["condition"].astype(str) == condition)]["value"]
            mean, ci = mean_ci(subset)
            means.append(mean)
            cis.append(ci)
            metrics["means"][f"{group}|{condition}"] = {"mean": mean, "ci95": ci, "n": len(subset)}
            jitter = rng.uniform(-width * 0.24, width * 0.24, len(subset))
            ax.scatter(np.full(len(subset), positions[groups.index(group)]) + jitter, subset, s=8, color="#222222", alpha=0.42, zorder=3)
        ax.bar(positions, means, width=width * 0.88, yerr=cis, capsize=2.2, color=colors[index], alpha=0.82, label=condition, edgecolor="#333333", linewidth=0.45, hatch=hatches[index])
    ax.set_xticks(np.arange(len(groups)), groups)
    ax.set_ylabel("Response (a.u.)")
    ax.legend(ncol=min(3, len(conditions)), loc="upper left")
    return metrics


def render_line(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    metrics: dict[str, Any] = {"series": {}}
    markers = ["o", "s", "^", "D", "v", "P"]
    linestyles = ["-", "--", "-.", ":", (0, (5, 1)), (0, (3, 1, 1, 1))]
    for index, (group, subset) in enumerate(data.groupby("group", sort=False)):
        summary = subset.groupby("x", sort=True)["value"].agg(["mean", "std", "count"]).reset_index()
        ci = 1.96 * summary["std"] / np.sqrt(summary["count"])
        x = summary["x"].to_numpy(dtype=float)
        mean = summary["mean"].to_numpy(dtype=float)
        ax.plot(x, mean, color=colors[index], marker=markers[index], linestyle=linestyles[index], markersize=3.2, linewidth=1.5, label=str(group))
        ax.fill_between(x, mean - ci, mean + ci, color=colors[index], alpha=0.16, linewidth=0)
        metrics["series"][str(group)] = summary.to_dict(orient="records")
    ax.set_xlabel("Time (day)")
    ax.set_ylabel("Response (a.u.)")
    ax.legend(loc="upper left")
    return metrics


def render_violin(data: pd.DataFrame, ax: plt.Axes, colors: Theme, rng: np.random.Generator) -> dict[str, Any]:
    groups = list(dict.fromkeys(data["group"].astype(str)))
    values = [data[data["group"].astype(str) == group]["value"].to_numpy(dtype=float) for group in groups]
    violin = ax.violinplot(values, showmeans=False, showmedians=False, showextrema=False)
    for index, body in enumerate(violin["bodies"]):
        body.set_facecolor(colors[index])
        body.set_edgecolor(colors[index])
        body.set_alpha(0.34)
    ax.boxplot(values, widths=0.16, patch_artist=True, showfliers=False, boxprops={"facecolor": "white", "edgecolor": "#333333", "linewidth": 0.8}, medianprops={"color": "#111111", "linewidth": 1.2}, whiskerprops={"color": "#333333", "linewidth": 0.8}, capprops={"color": "#333333", "linewidth": 0.8})
    for index, array in enumerate(values, start=1):
        ax.scatter(index + rng.uniform(-0.10, 0.10, len(array)), array, s=7, color=colors[index - 1], edgecolor="white", linewidth=0.25, alpha=0.65)
    ax.set_xticks(range(1, len(groups) + 1), groups)
    ax.set_ylabel("Response (a.u.)")
    return {"groups": {group: {"n": len(array), "median": float(np.median(array))} for group, array in zip(groups, values, strict=True)}}


def render_correlation(data: pd.DataFrame, ax: plt.Axes, colors: Theme, __: np.random.Generator) -> dict[str, Any]:
    corr = data.select_dtypes(include="number").corr()
    cmap = LinearSegmentedColormap.from_list(f"{colors.theme_id}-diverging", colors.diverging, N=256)
    image = ax.imshow(corr, vmin=-1, vmax=1, cmap=cmap)
    for row in range(len(corr)):
        for col in range(len(corr)):
            value = corr.iloc[row, col]
            ax.text(col, row, f"{value:.2f}", ha="center", va="center", color="white" if abs(value) > 0.58 else "#222222", fontsize=5.5)
    ax.set_xticks(range(len(corr)), corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr)), corr.columns)
    colorbar = ax.figure.colorbar(image, ax=ax, fraction=0.045, pad=0.04)
    colorbar.set_label("Pearson r")
    return {"correlation": corr.round(8).to_dict()}


def render_pca(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    features = data.drop(columns=["sample_id", "group"]).select_dtypes(include="number")
    matrix = (features - features.mean()) / features.std(ddof=1)
    u, singular, vt = np.linalg.svd(matrix.to_numpy(), full_matrices=False)
    scores = u[:, :2] * singular[:2]
    variance = singular**2 / np.sum(singular**2)
    markers = ["o", "s", "^", "D", "v", "P"]
    for index, group in enumerate(dict.fromkeys(data["group"].astype(str))):
        mask = data["group"].astype(str).to_numpy() == group
        ax.scatter(scores[mask, 0], scores[mask, 1], s=23, marker=markers[index], color=colors[index], alpha=0.78, label=group, edgecolor="white", linewidth=0.4)
    scale = np.percentile(np.abs(scores[:, :2]), 82)
    for index, name in enumerate(features.columns):
        x, y = vt[0, index] * scale, vt[1, index] * scale
        ax.annotate("", (x, y), (0, 0), arrowprops={"arrowstyle": "->", "color": "#555555", "lw": 0.8})
        ax.text(x * 1.08, y * 1.08, name, fontsize=5.5, ha="center", va="center")
    ax.axhline(0, color="#DDDDDD", linewidth=0.6, zorder=0)
    ax.axvline(0, color="#DDDDDD", linewidth=0.6, zorder=0)
    ax.set_xlabel(f"PC1 ({variance[0] * 100:.1f}%)")
    ax.set_ylabel(f"PC2 ({variance[1] * 100:.1f}%)")
    ax.legend(loc="best")
    return {"explained_variance": variance[:2].tolist(), "feature_columns": list(features.columns)}


def render_forest(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    ordered = data.iloc[::-1].reset_index(drop=True)
    y = np.arange(len(ordered))
    estimate = ordered["estimate"].to_numpy(dtype=float)
    lower = ordered["lower"].to_numpy(dtype=float)
    upper = ordered["upper"].to_numpy(dtype=float)
    ax.errorbar(estimate, y, xerr=[estimate - lower, upper - estimate], fmt="o", color=colors[0], ecolor="#4D4D4D", elinewidth=1.1, capsize=2.5, markersize=4.3)
    ax.axvline(0, color="#777777", linestyle="--", linewidth=0.8)
    ax.set_yticks(y, ordered["label"].astype(str))
    ax.set_xlabel("Effect estimate (95% CI)")
    return {"effects": ordered.to_dict(orient="records")}


def binary_curves(data: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    ordered = data.sort_values("score", ascending=False)
    y = ordered["y_true"].to_numpy(dtype=int)
    positives = y.sum()
    negatives = len(y) - positives
    if positives == 0 or negatives == 0:
        raise ValueError("Binary evaluation requires both positive and negative observations")
    tp = np.cumsum(y)
    fp = np.cumsum(1 - y)
    tpr = np.r_[0.0, tp / positives, 1.0]
    fpr = np.r_[0.0, fp / negatives, 1.0]
    recall = np.r_[0.0, tp / positives, 1.0]
    precision = np.r_[1.0, tp / np.arange(1, len(y) + 1), positives / len(y)]
    return fpr, tpr, recall, precision


def render_roc(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    fpr, tpr, _, _ = binary_curves(data)
    auc = float(np.trapezoid(tpr, fpr))
    ax.plot(fpr, tpr, color=colors[0], linewidth=1.8, label=f"Model (AUROC={auc:.3f})")
    ax.plot([0, 1], [0, 1], color="#777777", linestyle="--", linewidth=0.8, label="Chance")
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="False-positive rate", ylabel="True-positive rate")
    ax.legend(loc="lower right")
    return {"auroc": auc, "n": len(data), "positive_n": int(data["y_true"].sum())}


def render_pr(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    _, _, recall, precision = binary_curves(data)
    # Average precision follows the right-continuous step definition, not trapezoidal interpolation.
    ap = float(np.sum(np.diff(recall) * precision[1:]))
    prevalence = float(data["y_true"].mean())
    ax.step(recall, precision, where="post", color=colors.accent, linewidth=1.8, label=f"Model (AUPRC={ap:.3f})")
    ax.axhline(prevalence, color="#777777", linestyle="--", linewidth=0.8, label=f"Prevalence={prevalence:.2f}")
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Recall", ylabel="Precision")
    ax.legend(loc="lower left")
    return {"auprc": ap, "prevalence": prevalence, "n": len(data)}


def render_calibration(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    work = data.copy()
    work["bin"] = pd.cut(work["score"], bins=np.linspace(0, 1, 11), include_lowest=True, labels=False)
    summary = work.groupby("bin", observed=True).agg(predicted=("score", "mean"), observed=("y_true", "mean"), n=("y_true", "size")).dropna()
    ax.plot([0, 1], [0, 1], color="#777777", linestyle="--", linewidth=0.8, label="Ideal")
    ax.plot(summary["predicted"], summary["observed"], color=colors[2], marker="o", linewidth=1.5, label="Model")
    for _, row in summary.iterrows():
        ax.scatter(row["predicted"], row["observed"], s=10 + 1.4 * row["n"], color=colors[2], alpha=0.35, edgecolor="none")
    brier = float(np.mean((data["score"] - data["y_true"]) ** 2))
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Mean predicted probability", ylabel="Observed event fraction")
    ax.legend(loc="upper left", title=f"Brier={brier:.3f}")
    return {"brier_score": brier, "bins": summary.reset_index().to_dict(orient="records")}


def render_volcano(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    work = data.copy()
    work["neg_log10_p"] = -np.log10(work["p_value"].clip(lower=np.finfo(float).tiny))
    significant = (work["p_value"] < 0.05) & (work["log2fc"].abs() >= 1)
    up = significant & (work["log2fc"] > 0)
    down = significant & (work["log2fc"] < 0)
    ax.scatter(work.loc[~significant, "log2fc"], work.loc[~significant, "neg_log10_p"], s=9, color="#BDBDBD", alpha=0.55, label="Not significant")
    ax.scatter(work.loc[down, "log2fc"], work.loc[down, "neg_log10_p"], s=12, color=colors.diverging[0], alpha=0.75, label="Down")
    ax.scatter(work.loc[up, "log2fc"], work.loc[up, "neg_log10_p"], s=12, color=colors.diverging[-1], alpha=0.75, label="Up")
    ax.axvline(-1, color="#777777", linestyle="--", linewidth=0.7)
    ax.axvline(1, color="#777777", linestyle="--", linewidth=0.7)
    ax.axhline(-math.log10(0.05), color="#777777", linestyle="--", linewidth=0.7)
    for _, row in work.loc[significant].nlargest(5, "neg_log10_p").iterrows():
        ax.annotate(str(row["feature"]), (row["log2fc"], row["neg_log10_p"]), xytext=(3, 3), textcoords="offset points", fontsize=5.5)
    ax.set_xlabel("log2 fold change")
    ax.set_ylabel("−log10(p value)")
    ax.legend(loc="upper left")
    return {"significant_n": int(significant.sum()), "up_n": int(up.sum()), "down_n": int(down.sum())}


def km_curve(subset: pd.DataFrame) -> tuple[list[float], list[float], list[float], list[float]]:
    ordered = subset.sort_values("time")
    survival = 1.0
    xs, ys = [0.0], [1.0]
    censor_x, censor_y = [], []
    for time in sorted(ordered["time"].unique()):
        at_risk = int((ordered["time"] >= time).sum())
        events = int(((ordered["time"] == time) & (ordered["event"] == 1)).sum())
        censored = int(((ordered["time"] == time) & (ordered["event"] == 0)).sum())
        xs.extend([float(time), float(time)])
        ys.extend([survival, survival * (1 - events / at_risk) if at_risk else survival])
        survival = ys[-1]
        if censored:
            censor_x.extend([float(time)] * censored)
            censor_y.extend([survival] * censored)
    return xs, ys, censor_x, censor_y


def render_km(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    metrics: dict[str, Any] = {"groups": {}}
    max_time = float(data["time"].max())
    linestyles = ["-", "--", "-.", ":", (0, (5, 1)), (0, (3, 1, 1, 1))]
    censor_markers = ["|", "+", "x", "1", "2", "3"]
    for index, (group, subset) in enumerate(data.groupby("group", sort=False)):
        xs, ys, cx, cy = km_curve(subset)
        ax.step(xs, ys, where="post", color=colors[index], linestyle=linestyles[index], linewidth=1.7, label=f"{group} (n={len(subset)})")
        ax.plot(cx, cy, linestyle="none", marker=censor_markers[index], markersize=5, color=colors[index])
        metrics["groups"][str(group)] = {"n": len(subset), "events": int(subset["event"].sum())}
    ax.set(xlim=(0, max_time * 1.03), ylim=(0, 1.02), xlabel="Time (month)", ylabel="Survival probability")
    ax.legend(loc="lower left")
    return metrics


def render_sankey(data: pd.DataFrame, ax: plt.Axes, colors: Theme, _: np.random.Generator) -> dict[str, Any]:
    sources = list(dict.fromkeys(data["source"].astype(str)))
    targets = list(dict.fromkeys(data["target"].astype(str)))
    source_total = data.groupby("source", sort=False)["value"].sum().reindex(sources)
    target_total = data.groupby("target", sort=False)["value"].sum().reindex(targets)
    total = float(data["value"].sum())
    gap = 0.035

    def positions(values: pd.Series) -> dict[str, tuple[float, float]]:
        usable = 1 - gap * (len(values) - 1)
        cursor = 1.0
        result: dict[str, tuple[float, float]] = {}
        for label, value in values.items():
            height = usable * float(value) / total
            result[str(label)] = (cursor - height, cursor)
            cursor -= height + gap
        return result

    left = positions(source_total)
    right = positions(target_total)
    left_cursor = {key: value[0] for key, value in left.items()}
    right_cursor = {key: value[0] for key, value in right.items()}
    for index, row in data.iterrows():
        source, target, value = str(row["source"]), str(row["target"]), float(row["value"])
        height = (1 - gap * (len(sources) - 1)) * value / total
        y0a, y0b = left_cursor[source], left_cursor[source] + height
        y1a, y1b = right_cursor[target], right_cursor[target] + height
        vertices = [(0.14, y0a), (0.42, y0a), (0.58, y1a), (0.86, y1a), (0.86, y1b), (0.58, y1b), (0.42, y0b), (0.14, y0b), (0.14, y0a)]
        codes = [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4, MplPath.LINETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4, MplPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MplPath(vertices, codes), facecolor=colors[index % len(colors)], alpha=0.38, edgecolor="none"))
        left_cursor[source] = y0b
        right_cursor[target] = y1b
    for index, (label, (bottom, top)) in enumerate(left.items()):
        ax.add_patch(Rectangle((0.10, bottom), 0.04, top - bottom, facecolor=colors[index % len(colors)], edgecolor="white", linewidth=0.5))
        ax.text(0.085, (bottom + top) / 2, label, ha="right", va="center")
    for index, (label, (bottom, top)) in enumerate(right.items()):
        ax.add_patch(Rectangle((0.86, bottom), 0.04, top - bottom, facecolor=colors[(index + 2) % len(colors)], edgecolor="white", linewidth=0.5))
        ax.text(0.915, (bottom + top) / 2, label, ha="left", va="center")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    return {"total_flow": total, "links": data.to_dict(orient="records")}


RENDERERS: dict[str, Callable[[pd.DataFrame, plt.Axes, Theme, np.random.Generator], dict[str, Any]]] = {
    "grouped-bar-chart": render_grouped_bar,
    "line-chart": render_line,
    "violin-plot": render_violin,
    "correlation-matrix": render_correlation,
    "pca-biplot": render_pca,
    "forest-plot": render_forest,
    "roc-curve": render_roc,
    "precision-recall-curve": render_pr,
    "calibration-curve": render_calibration,
    "volcano-plot": render_volcano,
    "kaplan-meier-curve": render_km,
    "sankey-diagram": render_sankey,
}


def export_bundle(fig: plt.Figure, output_dir: Path, profile: str, metadata: dict[str, Any]) -> None:
    spec = PROFILES[profile]
    output_dir.mkdir(parents=True, exist_ok=True)
    png_path = output_dir / "figure.png"
    # 保留画布的精确物理尺寸；constrained_layout 负责内部留白，不在导出时再次裁切。
    save_kwargs: dict[str, Any] = {"facecolor": "white"}
    fig.savefig(output_dir / "figure.pdf", **save_kwargs)
    svg_path = output_dir / "figure.svg"
    fig.savefig(svg_path, **save_kwargs)
    # Matplotlib 会在 SVG 路径行末保留空格；规范化文本不改变几何语义，并保持 Git 审计干净。
    svg_lines = svg_path.read_text(encoding="utf-8").splitlines()
    svg_path.write_text("\n".join(line.rstrip() for line in svg_lines) + "\n", encoding="utf-8")
    fig.savefig(png_path, dpi=spec["dpi"], **save_kwargs)
    with Image.open(png_path) as image:
        image.convert("L").save(output_dir / "figure-grayscale.png", dpi=image.info.get("dpi", (spec["dpi"], spec["dpi"])))
    (output_dir / "figure-metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output_dir / "alt-text.txt").write_text(metadata["alt_text"].strip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chart-id", required=True, choices=sorted(RENDERERS))
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--profile", choices=sorted(PROFILES), default="journal_print")
    parser.add_argument("--theme", choices=("auto", *THEME_IDS), default="auto")
    parser.add_argument("--seed", type=int, default=20260801)
    parser.add_argument("--font-family")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    required_outputs = ["figure.pdf", "figure.svg", "figure.png", "figure-grayscale.png", "figure-metadata.json", "alt-text.txt", "source-data.csv"]
    existing = [name for name in required_outputs if (output_dir / name).exists()]
    if existing and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite existing outputs: {existing}")
    config: dict[str, Any] = {}
    if args.config:
        config = json.loads(args.config.resolve().read_text(encoding="utf-8"))
    data = demo_data(args.chart_id, args.seed) if args.demo else pd.read_csv(args.input.resolve())
    validate_data(args.chart_id, data)
    output_dir.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_dir / "source-data.csv", index=False)
    font_family = select_font(args.font_family)
    theme_id = resolve_theme(args.chart_id, args.theme)
    colors = configure_style(args.profile, theme_id, font_family)
    rng = np.random.default_rng(args.seed)
    fig, ax = plt.subplots(figsize=PROFILES[args.profile]["figsize"], constrained_layout=True)
    metrics = RENDERERS[args.chart_id](data, ax, colors, rng)
    headline = str(config.get("headline", args.chart_id.replace("-", " ").title()))
    ax.set_title(headline, loc="left", fontweight="bold", pad=8)
    metadata = {
        "schema_version": "1.0.0",
        "renderer_version": VERIFIER_VERSION,
        "chart_id": args.chart_id,
        "profile": args.profile,
        "theme": theme_id,
        "font_family": font_family,
        "seed": args.seed,
        "source_mode": "demo" if args.demo else "input",
        "source_rows": len(data),
        "source_sha256": sha256_file(output_dir / "source-data.csv"),
        "palette": {
            "categorical": list(colors.categorical),
            "sequential": list(colors.sequential),
            "diverging": list(colors.diverging),
            "accent": colors.accent,
        },
        "metrics": metrics,
        "alt_text": str(config.get("alt_text", f"{headline}. The chart is based on {len(data)} source rows; consult figure-metadata.json for computed values and methods.")),
    }
    export_bundle(fig, output_dir, args.profile, metadata)
    plt.close(fig)
    print(json.dumps({"chart_id": args.chart_id, "output_dir": str(output_dir), "outputs": required_outputs}, ensure_ascii=False))


if __name__ == "__main__":
    main()
