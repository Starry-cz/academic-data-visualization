#!/usr/bin/env python3
"""Thresholded correlation network for multivariate observations.

Input CSV: observations in rows and numeric variables in columns. Edges encode
Pearson correlation sign by colour/line style and magnitude by width. Network
edges are associations, not causal links.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_qa import audit_figure


NODE_COLORS = ["#EEA599", "#FAC795", "#E3EDE0", "#ABD3E1", "#92B4C8", "#565AA7"]
POSITIVE = "#497AB7"
NEGATIVE = "#DA4139"


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
            "font.size": 8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.7,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
            "savefig.dpi": 450,
        }
    )


def demo_data() -> pd.DataFrame:
    rng = np.random.default_rng(729)
    latent = rng.normal(size=(90, 3))
    mixing = np.array(
        [
            [1.0, 0.0, 0.2],
            [0.8, 0.0, 0.1],
            [0.6, -0.2, 0.0],
            [0.0, 1.0, 0.1],
            [0.1, 0.75, 0.2],
            [0.0, -0.65, 0.3],
            [0.2, 0.0, 1.0],
            [-0.2, 0.1, 0.78],
            [0.35, 0.25, -0.55],
        ]
    )
    values = latent @ mixing.T + rng.normal(scale=0.36, size=(90, 9))
    return pd.DataFrame(values, columns=[f"V{i}" for i in range(1, 10)])


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    numeric = data.select_dtypes(include=np.number).copy()
    if numeric.shape[1] < 4 or numeric.shape[0] < 4:
        raise ValueError("at least four numeric variables and four observations are required")
    if not np.isfinite(numeric.to_numpy()).all():
        raise ValueError("numeric variables must be finite")
    if (numeric.nunique() < 2).any():
        raise ValueError("each numeric variable must contain variation")
    return numeric


def build_graph(data: pd.DataFrame, threshold: float) -> nx.Graph:
    if not 0 < threshold < 1:
        raise ValueError("threshold must be between 0 and 1")
    corr = validate_data(data).corr(method="pearson")
    graph = nx.Graph()
    graph.add_nodes_from(corr.columns)
    for i, source in enumerate(corr.columns):
        for target in corr.columns[i + 1 :]:
            value = float(corr.loc[source, target])
            if abs(value) >= threshold:
                graph.add_edge(source, target, correlation=value, weight=abs(value))
    if graph.number_of_edges() == 0:
        raise ValueError("no edges meet the requested threshold")
    return graph


def plot_correlation_network(data: pd.DataFrame, threshold: float = 0.45) -> plt.Figure:
    graph = build_graph(data, threshold)
    communities = list(nx.community.greedy_modularity_communities(graph, weight="weight"))
    community_of = {node: index for index, community in enumerate(communities) for node in community}
    if len(communities) > len(NODE_COLORS):
        raise ValueError(f"At most {len(NODE_COLORS)} communities are supported")

    # 环形布局让正负边和线宽编码在小型相关网络中更易比较，并保证重复渲染位置稳定。
    position = nx.circular_layout(graph, scale=0.82)
    strengths = {
        node: sum(edge["weight"] for _, _, edge in graph.edges(node, data=True))
        for node in graph.nodes
    }
    node_sizes = [300 + strengths[node] * 90 for node in graph.nodes]
    node_colors = [NODE_COLORS[community_of[node]] for node in graph.nodes]

    fig = plt.figure(figsize=(6.4, 4.7))
    grid = fig.add_gridspec(
        1, 2, width_ratios=[5.0, 1.4], left=0.03, right=0.98, bottom=0.12, top=0.87, wspace=0.02
    )
    ax = fig.add_subplot(grid[0, 0])
    legend_ax = fig.add_subplot(grid[0, 1])
    legend_ax.set_axis_off()
    positive = [(u, v) for u, v, d in graph.edges(data=True) if d["correlation"] > 0]
    negative = [(u, v) for u, v, d in graph.edges(data=True) if d["correlation"] < 0]
    for edges, color, style in [(positive, POSITIVE, "solid"), (negative, NEGATIVE, "dashed")]:
        nx.draw_networkx_edges(
            graph,
            position,
            edgelist=edges,
            width=[0.7 + 4.2 * graph.edges[edge]["weight"] for edge in edges],
            edge_color=color,
            style=style,
            alpha=0.62,
            ax=ax,
        )
    nx.draw_networkx_nodes(
        graph,
        position,
        node_size=node_sizes,
        node_color=node_colors,
        edgecolors="#FFFFFF",
        linewidths=1.2,
        ax=ax,
    )
    nx.draw_networkx_labels(graph, position, font_size=8, font_weight="bold", ax=ax)
    fig.suptitle(f"Correlation network | |r| ≥ {threshold:.2f}", y=0.96)
    ax.set_axis_off()
    legend_ax.legend(
        handles=[
            Line2D([0], [0], color=POSITIVE, lw=2.2, label="Positive association"),
            Line2D([0], [0], color=NEGATIVE, lw=2.2, ls="--", label="Negative association"),
        ],
        loc="center",
        ncol=1,
    )
    fig.text(0.5, 0.025, "Edge width encodes |Pearson r|; associations do not imply causation.",
             ha="center", fontsize=7, color="#5F6772")
    return fig


def save_figure(fig: plt.Figure, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    audit_figure(fig, output.stem)
    fig.savefig(output.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=450, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="CSV with observations × numeric variables")
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.45)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("correlation_network"))
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_correlation_network(data, args.threshold), args.output)


if __name__ == "__main__":
    main()
