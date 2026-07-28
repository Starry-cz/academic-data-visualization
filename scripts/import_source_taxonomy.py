#!/usr/bin/env python3
"""Import the supplied 24-category, 714-membership chart taxonomy."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any

from chart_registry_lib import REGISTRY_PATH, SOURCE_PATH, load_registry, normalize_alias


CATEGORIES = [
    ("01", "comparison-ranking", "数值比较与排序图", "Comparison and Ranking"),
    ("02", "time-trend-dynamics", "时间趋势与动态变化图", "Time Trends and Dynamics"),
    ("03", "distribution", "数据分布图", "Data Distribution"),
    ("04", "relationship-correlation", "变量关系与相关性图", "Relationships and Correlation"),
    ("05", "composition-proportion", "构成、比例与整体—部分关系图", "Composition and Part-to-whole"),
    ("06", "uncertainty-effect-size", "统计估计、效应量与不确定性图", "Estimation, Effect Size, and Uncertainty"),
    ("07", "experimental-design-group-differences", "实验设计与组间差异图", "Experimental Design and Group Differences"),
    ("08", "regression-model-diagnostics", "回归与统计模型诊断图", "Regression and Statistical Model Diagnostics"),
    ("09", "classification-prediction-machine-learning", "分类、预测与机器学习评估图", "Classification, Prediction, and Machine Learning"),
    ("10", "hierarchy-classification", "层级与分类结构图", "Hierarchy and Classification Structure"),
    ("11", "network-relationship-structure", "网络与关系结构图", "Networks and Relational Structure"),
    ("12", "flow-migration", "流程、迁移与流量图", "Process, Transition, and Flow"),
    ("13", "spatial-geographic", "空间与地理数据图", "Spatial and Geographic Data"),
    ("14", "high-dimensional-multivariate", "高维与多变量数据图", "High-dimensional and Multivariate Data"),
    ("15", "qualitative-text-analysis", "质性研究与文本分析图", "Qualitative Research and Text Analysis"),
    ("16", "education-psychometrics", "教育学与心理测量常用图", "Education and Psychometrics"),
    ("17", "medicine-public-health-life-sciences", "医学、公共卫生与生命科学常用图", "Medicine, Public Health, and Life Sciences"),
    ("18", "sets-overlap-combinations", "集合、重叠与分类组合图", "Sets, Overlap, and Category Combinations"),
    ("19", "three-dimensional-scientific-computing", "三维、曲面与科学计算图", "3D, Surface, and Scientific Computing"),
    ("20", "engineering-quality-process-control", "工程、质量管理与过程控制图", "Engineering, Quality, and Process Control"),
    ("21", "bibliometrics-science-mapping", "文献计量与科学知识图谱", "Bibliometrics and Science Mapping"),
    ("22", "causal-theoretical-models", "因果机制与理论模型图", "Causal Mechanisms and Theoretical Models"),
    ("23", "research-process-paper-standards", "研究流程与论文规范图", "Research Process and Reporting Standards"),
    ("24", "composite-advanced", "复合图与高级科研图形", "Composite and Advanced Scientific Figures"),
]


CATEGORY_PROFILES: dict[str, dict[str, Any]] = {
    "01": {
        "task": "比较对象、组别或指标的大小、排序与差值",
        "unit": "类别、对象或实验条件",
        "required": ["category", "value"],
        "optional": ["group", "uncertainty", "label"],
        "types": ["categorical", "quantitative"],
        "encoding": ["共同尺度上的位置或长度", "必要时以颜色或形状区分组别"],
        "disciplines": ["general"],
        "status": "reusable_pattern",
    },
    "02": {
        "task": "展示变量随时间、阶段、年龄或实验轮次的变化",
        "unit": "时间点、阶段或纵向观测",
        "required": ["ordered_time", "value"],
        "optional": ["group", "uncertainty", "event"],
        "types": ["temporal", "quantitative"],
        "encoding": ["横轴表示有序时间", "位置、线或带表示数值与不确定性"],
        "disciplines": ["general", "longitudinal research"],
        "status": "reusable_pattern",
    },
    "03": {
        "task": "检查分布形态、离散程度、偏态、多峰与异常值",
        "unit": "个体观测或样本",
        "required": ["value"],
        "optional": ["group", "weight", "identifier"],
        "types": ["quantitative"],
        "encoding": ["位置、密度、频数或分位数", "分组时保持共同尺度"],
        "disciplines": ["general", "statistics"],
        "status": "reusable_pattern",
    },
    "04": {
        "task": "评估变量之间的方向、强度、形态与非线性关系",
        "unit": "配对观测或变量组合",
        "required": ["x", "y"],
        "optional": ["group", "weight", "facet", "uncertainty"],
        "types": ["quantitative", "categorical"],
        "encoding": ["二维位置", "颜色、大小或分面表示附加变量"],
        "disciplines": ["general", "statistics"],
        "status": "reusable_pattern",
    },
    "05": {
        "task": "展示组成比例以及整体与部分之间的关系",
        "unit": "整体中的类别或层级单元",
        "required": ["category", "value_or_proportion"],
        "optional": ["parent", "group", "label"],
        "types": ["categorical", "quantitative", "hierarchical"],
        "encoding": ["长度、面积或角度表示组成", "总和与分母必须明确"],
        "disciplines": ["general"],
        "status": "reusable_pattern",
    },
    "06": {
        "task": "报告估计值、效应量与统计不确定性",
        "unit": "参数、效应或比较项",
        "required": ["estimate", "interval"],
        "optional": ["group", "reference", "distribution"],
        "types": ["quantitative", "statistical estimate"],
        "encoding": ["点或分布表示估计", "线段或带表示区间"],
        "disciplines": ["statistics", "evidence synthesis"],
        "status": "reusable_pattern",
    },
    "07": {
        "task": "表达实验设计、前后测、重复测量与组间差异",
        "unit": "受试者、实验单元或组别",
        "required": ["condition", "outcome"],
        "optional": ["subject_id", "time", "group", "uncertainty"],
        "types": ["categorical", "quantitative", "paired_or_repeated"],
        "encoding": ["组别位置与连接关系", "保留个体或区间证据"],
        "disciplines": ["experimental research", "causal inference"],
        "status": "reusable_pattern",
    },
    "08": {
        "task": "诊断回归与统计模型的拟合、残差、影响点和假设",
        "unit": "样本、模型、参数或阈值",
        "required": ["model_output", "diagnostic_measure"],
        "optional": ["observed", "predicted", "group", "threshold"],
        "types": ["model output", "quantitative"],
        "encoding": ["诊断量的位置、路径或矩阵", "明确参考线和异常阈值"],
        "disciplines": ["statistics", "modeling"],
        "status": "reusable_pattern",
    },
    "09": {
        "task": "评估分类、预测、聚类和机器学习模型",
        "unit": "样本、模型、阈值、特征或聚类",
        "required": ["model_output", "target_or_metric"],
        "optional": ["class", "threshold", "feature", "fold"],
        "types": ["model output", "categorical", "quantitative"],
        "encoding": ["性能、误差或解释量的位置与颜色", "比较时使用一致评估集"],
        "disciplines": ["machine learning", "data science"],
        "status": "on_demand",
    },
    "10": {
        "task": "展示层级、分类、聚类或谱系结构",
        "unit": "节点、类别或层级单元",
        "required": ["node", "parent_or_distance"],
        "optional": ["value", "group", "label"],
        "types": ["hierarchical", "categorical"],
        "encoding": ["嵌套、分支或空间包含关系", "层级深度必须可辨识"],
        "disciplines": ["general", "taxonomy"],
        "status": "on_demand",
    },
    "11": {
        "task": "展示实体之间的连接、权重、社群与网络结构",
        "unit": "节点与边",
        "required": ["source", "target"],
        "optional": ["edge_weight", "node_group", "time"],
        "types": ["graph", "categorical", "quantitative"],
        "encoding": ["节点位置与连线", "大小、颜色或线宽表示属性"],
        "disciplines": ["network science", "social science"],
        "status": "on_demand",
    },
    "12": {
        "task": "展示流程、状态迁移、路径和流量",
        "unit": "阶段、状态、路径或流",
        "required": ["source_or_stage", "target_or_next_stage"],
        "optional": ["flow_value", "time", "group"],
        "types": ["flow", "sequence", "categorical"],
        "encoding": ["方向、连线与宽度", "所有流量必须可追溯"],
        "disciplines": ["process research", "operations"],
        "status": "on_demand",
    },
    "13": {
        "task": "展示地理位置、区域差异、空间模式与空间过程",
        "unit": "坐标、区域、栅格或空间对象",
        "required": ["geometry_or_coordinates", "value"],
        "optional": ["time", "group", "uncertainty"],
        "types": ["geospatial", "quantitative", "categorical"],
        "encoding": ["地理位置、颜色、大小或流向", "必须声明坐标系和空间尺度"],
        "disciplines": ["geography", "spatial science"],
        "status": "on_demand",
    },
    "14": {
        "task": "揭示高维、多变量与降维后的结构",
        "unit": "样本、变量或低维嵌入点",
        "required": ["multivariate_matrix"],
        "optional": ["group", "loading", "distance", "annotation"],
        "types": ["multivariate", "matrix", "quantitative"],
        "encoding": ["多个轴、矩阵或低维位置", "说明标准化和降维参数"],
        "disciplines": ["multivariate statistics", "data science"],
        "status": "on_demand",
    },
    "15": {
        "task": "展示质性编码、文本主题、语义关系与叙事结构",
        "unit": "文本、文档、编码、主题或案例",
        "required": ["text_unit_or_code", "frequency_or_relation"],
        "optional": ["time", "group", "sentiment", "quotation"],
        "types": ["text", "categorical", "network"],
        "encoding": ["频数、矩阵、关系或时间结构", "保留语料与编码可追溯性"],
        "disciplines": ["qualitative research", "text analysis"],
        "status": "on_demand",
    },
    "16": {
        "task": "表达教育测量、心理计量、学习过程与学校效应",
        "unit": "学生、题目、班级、学校或潜变量",
        "required": ["measurement_or_learning_output"],
        "optional": ["person", "item", "time", "group"],
        "types": ["psychometric", "multilevel", "longitudinal"],
        "encoding": ["参数、轨迹、路径或矩阵", "说明量尺、模型与层级"],
        "disciplines": ["education", "psychometrics"],
        "status": "on_demand",
    },
    "17": {
        "task": "表达临床、生存、流行病学、基因组与生命科学证据",
        "unit": "患者、事件、样本、基因、细胞或通路",
        "required": ["biomedical_measure_or_model_output"],
        "optional": ["group", "time", "event", "annotation"],
        "types": ["biomedical", "survival", "omics"],
        "encoding": ["按领域量尺编码位置、区间、网络或矩阵", "保留临床与组学注释"],
        "disciplines": ["medicine", "public health", "life sciences"],
        "status": "on_demand",
    },
    "18": {
        "task": "展示集合成员、交集、重叠与分类组合",
        "unit": "集合、成员或组合",
        "required": ["set_membership"],
        "optional": ["set_size", "intersection_size", "group"],
        "types": ["set", "binary", "categorical"],
        "encoding": ["区域、矩阵或条形表示集合关系", "集合较多时优先矩阵编码"],
        "disciplines": ["general", "bioinformatics"],
        "status": "reusable_pattern",
    },
    "19": {
        "task": "展示三维场、曲面、体数据与科学计算结果",
        "unit": "三维坐标、网格、体素或场变量",
        "required": ["spatial_coordinates_or_mesh", "field_value"],
        "optional": ["time", "vector_components", "material"],
        "types": ["three-dimensional", "mesh", "field"],
        "encoding": ["三维位置、曲面、切片、等值面或矢量", "提供尺度与视角说明"],
        "disciplines": ["engineering", "scientific computing"],
        "status": "on_demand",
    },
    "20": {
        "task": "监控工程质量、过程稳定性、可靠性与风险",
        "unit": "过程批次、样本、部件或失效事件",
        "required": ["process_or_reliability_measure"],
        "optional": ["time", "subgroup", "specification_limit"],
        "types": ["process", "reliability", "quantitative"],
        "encoding": ["时间、控制界限、分布或风险矩阵", "必须区分控制限与规格限"],
        "disciplines": ["engineering", "quality management"],
        "status": "on_demand",
    },
    "21": {
        "task": "展示文献计量关系、知识结构、主题与研究前沿",
        "unit": "文献、作者、机构、关键词、主题或引文",
        "required": ["bibliographic_entity_or_relation"],
        "optional": ["time", "citation_count", "cluster"],
        "types": ["bibliometric", "network", "temporal"],
        "encoding": ["网络、时间、流向或战略坐标", "说明数据库、检索式与阈值"],
        "disciplines": ["bibliometrics", "science mapping"],
        "status": "on_demand",
    },
    "22": {
        "task": "表达因果机制、理论关系、路径与逻辑模型",
        "unit": "概念、变量、机制、路径或系统状态",
        "required": ["concept_or_variable", "relationship"],
        "optional": ["level", "direction", "hypothesis", "evidence"],
        "types": ["conceptual", "causal", "graph"],
        "encoding": ["节点、方向和关系类型", "区分假设、证据与因果主张"],
        "disciplines": ["theory building", "causal research"],
        "status": "on_demand",
    },
    "23": {
        "task": "说明研究流程、报告规范、实验步骤与系统架构",
        "unit": "研究阶段、样本步骤、模块或方法单元",
        "required": ["step_or_component", "sequence_or_relation"],
        "optional": ["decision", "count", "time", "owner"],
        "types": ["process", "diagram", "sequence"],
        "encoding": ["方向、层级、步骤和模块边界", "流程节点必须与正文一致"],
        "disciplines": ["research methods", "reporting standards"],
        "status": "on_demand",
    },
    "24": {
        "task": "整合多个证据层、图型或模态形成复合科研图",
        "unit": "面板、图层、模态或证据模块",
        "required": ["multiple_evidence_layers"],
        "optional": ["shared_scale", "panel_label", "annotation"],
        "types": ["composite", "multimodal"],
        "encoding": ["面板布局与跨面板对齐", "共享尺度和阅读顺序必须明确"],
        "disciplines": ["general", "scientific communication"],
        "status": "on_demand",
    },
}


OLD_CATEGORY_REMAP = {
    "01": "01", "02": "02", "03": "03", "04": "04", "05": "14", "06": "14",
    "07": "06", "08": "08", "09": "09", "10": "05", "11": "18", "12": "12",
    "13": "11", "14": "13", "15": "17", "16": "17", "17": "17", "18": "17",
    "19": "17", "20": "16", "21": "07", "22": "21", "23": "20", "24": "24",
}


# 明确的语义合并优先于字符串相似度，尤其保护已有生产资产的 canonical ID。
LABEL_ID_OVERRIDES = {
    "柱状图": "categorical-bar-chart",
    "多序列折线图": "line-chart",
    "密度图": "kernel-density-plot",
    "核密度估计图": "kernel-density-plot",
    "ECDF图": "ecdf-plot",
    "正态概率图": "qq-plot",
    "带回归线散点图": "scatter-regression-plot",
    "气泡图": "bubble-scatter",
    "相关矩阵图": "correlation-matrix",
    "相关热力图": "correlation-matrix",
    "相关圆图": "correlation-matrix",
    "边际分布散点图": "marginal-density-scatter",
    "六边形散点密度图": "hexbin-plot",
    "双变量直方图": "two-dimensional-histogram",
    "人口分布金字塔图": "population-pyramid",
    "人口金字塔图": "population-pyramid",
    "百分比堆积柱状图": "percent-stacked-bar-chart",
    "百分比堆积面积图": "percent-stacked-area-chart",
    "点—区间图": "interval-plot",
    "校准图": "calibration-curve",
    "PR曲线": "precision-recall-curve",
    "PDP图": "partial-dependence-plot",
    "ICE图": "ice-plot",
    "排列重要性图": "permutation-importance-plot",
    "PCA图": "pca-biplot",
    "主成分双标图": "pca-biplot",
    "结构方程模型路径图": "sem-path-diagram",
    "组间小提琴图": "grouped-violin-plot",
    "Kaplan–Meier生存曲线": "kaplan-meier-curve",
    "累积风险曲线": "cumulative-hazard-curve",
    "累积发生函数图": "cumulative-incidence-curve",
    "基因组浏览器轨迹图": "genome-browser-track",
    "GSEA曲线": "gsea-curve",
    "系统发育树": "phylogenetic-tree",
    "Venn图": "venn-diagram",
    "Euler图": "euler-diagram",
    "集合矩阵图": "set-matrix",
    "PCA得分图": "pca-score-plot",
    "PCA载荷图": "pca-loading-plot",
    "协变量平衡图": "love-plot",
    "差异中的差异图": "difference-in-differences-plot",
    "间断时间序列图": "interrupted-time-series",
    "关键词突现图": "keyword-burst-plot",
    "文献耦合图": "bibliographic-coupling-network",
    "主题图": "thematic-map",
    "Grand Tour动态图": "grand-tour",
    "双曲树图": "hyperbolic-tree",
    "体渲染图": "volume-rendering",
    "等值面图": "isosurface",
    "三维矢量场图": "three-dimensional-vector-field",
    "流程挖掘图": "complex-process-mining",
    "树状图": "hierarchy-tree",
    "曲面图": "three-dimensional-surface",
    "三维曲面图": "three-dimensional-surface",
    "热力地图": "spatial-heatmap",
    "气泡地图": "proportional-symbol-map",
    "因果图": "causal-dag",
}


ENTRY_ID_OVERRIDES = {
    ("01", "棒棒糖图"): "lollipop-chart",
    ("01", "瀑布图"): "contribution-waterfall-chart",
    ("01", "雷达图／蜘蛛图"): "radar-chart",
    ("06", "漏斗图"): "meta-analysis-funnel-plot",
    ("12", "漏斗图"): "conversion-funnel-chart",
    ("17", "漏斗图"): "meta-analysis-funnel-plot",
    ("17", "瀑布图"): "tumor-response-waterfall-plot",
    ("17", "蜘蛛图"): "tumor-burden-spider-plot",
    ("21", "战略坐标图"): "strategic-diagram",
}

ENTRY_CANONICAL_NAMES = {
    ("17", "瀑布图（肿瘤疗效）"): ("肿瘤疗效瀑布图", "Tumor Response Waterfall Plot"),
    ("17", "蜘蛛图（肿瘤负荷变化）"): ("肿瘤负荷蜘蛛图", "Tumor Burden Spider Plot"),
}


MERGE_EXISTING_IDS = {
    # 两条旧记录语义相同；保留更明确的文献计量 canonical ID。
    "thematic-map": "strategic-diagram",
}


FULL_ENGLISH_NAMES = {
    "ALE图": "Accumulated Local Effects Plot",
    "Bode图": "Bode Plot",
    "Bradford分区图": "Bradford Zones Plot",
    "CONSORT流程图": "CONSORT Flow Diagram",
    "Cp/Cpk图": "Cp and Cpk Plot",
    "DIF项目图": "Differential Item Functioning Plot",
    "GSEA曲线": "Gene Set Enrichment Analysis Curve",
    "ICE图": "Individual Conditional Expectation Plot",
    "IPO模型图": "Input–Process–Output Model Diagram",
    "KS图": "Kolmogorov–Smirnov Plot",
    "KS曲线": "Kolmogorov–Smirnov Curve",
    "LASSO系数路径图": "LASSO Coefficient Path Plot",
    "LIME解释图": "LIME Explanation Plot",
    "LISA聚类地图": "Local Indicators of Spatial Association Cluster Map",
    "MA图": "MA Plot",
    "Moran散点图": "Moran Scatter Plot",
    "Mutation Landscape": "Mutation Landscape",
    "Nelson–Aalen曲线": "Nelson–Aalen Curve",
    "Nyquist图": "Nyquist Plot",
    "Oncoplot": "Oncoplot",
    "PCA图": "Principal Component Analysis Plot",
    "PCA得分图": "PCA Score Plot",
    "PCA载荷图": "PCA Loading Plot",
    "PDP图": "Partial Dependence Plot",
    "PRISMA流程图": "PRISMA Flow Diagram",
    "PR曲线": "Precision–Recall Curve",
    "Pixel-oriented Visualization": "Pixel-oriented Visualization",
    "Q矩阵热力图": "Q-matrix Heatmap",
    "ROC曲线": "Receiver Operating Characteristic Curve",
    "ROC空间图": "ROC Space Plot",
    "ROC置信区间图": "ROC Confidence Interval Plot",
    "Rasch项目地图": "Rasch Item Map",
    "SHAP依赖图": "SHAP Dependence Plot",
    "SHAP摘要图": "SHAP Summary Plot",
    "SHAP瀑布图": "SHAP Waterfall Plot",
    "SHAP蜂群图": "SHAP Beeswarm Plot",
    "SOM自组织映射图": "Self-organizing Map",
    "STROBE研究流程图": "STROBE Study Flow Diagram",
    "Smith圆图": "Smith Chart",
    "Theory of Change图": "Theory of Change Diagram",
    "UMAP图": "UMAP Plot",
    "UpSet图": "UpSet Plot",
    "VIF图": "Variance Inflation Factor Plot",
    "Venn图": "Venn Diagram",
    "Voronoi地图": "Voronoi Map",
    "Voronoi层级图": "Voronoi Hierarchy Diagram",
    "Voronoi树图": "Voronoi Treemap",
    "Weibull概率图": "Weibull Probability Plot",
    "X-bar控制图": "X-bar Control Chart",
    "t-SNE图": "t-SNE Plot",
    "二维核密度图": "Two-dimensional Kernel Density Plot",
    "典型相关图": "Canonical Correlation Plot",
    "南丁格尔玫瑰图": "Nightingale Rose Chart",
    "OR值森林图": "Odds Ratio Forest Plot",
    "RR值森林图": "Risk Ratio Forest Plot",
    "交叉验证结果图": "Cross-validation Results Plot",
    "校准曲线": "Calibration Curve",
    "决策曲线": "Decision Curve",
    "累积增益图": "Cumulative Gains Chart",
    "验证曲线": "Validation Curve",
    "决策树图": "Decision Tree Diagram",
    "规则提取图": "Rule Extraction Plot",
    "误差分析矩阵": "Error Analysis Matrix",
    "特征交互图": "Feature Interaction Plot",
    "作者合作网络图": "Author Collaboration Network",
    "机构合作网络图": "Institution Collaboration Network",
    "国家合作网络图": "Country Collaboration Network",
    "关联规则网络图": "Association Rule Network",
    "网络度分布图": "Network Degree Distribution Plot",
    "Alluvial网络演化图": "Alluvial Network Evolution Diagram",
    "马尔可夫转移图": "Markov Transition Diagram",
    "能量流图": "Energy Flow Diagram",
    "物质流图": "Material Flow Diagram",
    "事件序列图": "Event Sequence Plot",
    "漏斗转化图": "Conversion Funnel Chart",
    "Cartogram变形地图": "Cartogram",
    "时空轨迹图": "Spatiotemporal Trajectory Plot",
    "空间自相关图": "Spatial Autocorrelation Plot",
    "时间滑块地图": "Time-slider Map",
    "泰森多边形图": "Thiessen Polygon Map",
    "平行坐标图": "Parallel Coordinates Plot",
    "雷达图": "Radar Chart",
    "散点矩阵": "Scatterplot Matrix",
    "双标图": "Biplot",
    "平行集合图": "Parallel Sets Diagram",
    "多变量密度图": "Multivariate Density Plot",
    "词频条形图": "Word-frequency Bar Chart",
    "主题桑基图": "Theme Sankey Diagram",
    "情感雷达图": "Sentiment Radar Chart",
    "叙事时间轴": "Narrative Timeline",
    "案例比较矩阵": "Case Comparison Matrix",
    "证据链图": "Evidence Chain Diagram",
    "前后测配对图": "Pretest–posttest Paired Plot",
    "成长曲线图": "Growth Curve",
    "交互作用图": "Interaction Plot",
    "雷达能力画像图": "Radar Ability Profile",
    "学习者画像聚类图": "Learner Profile Cluster Plot",
    "学习路径桑基图": "Learning Path Sankey Diagram",
    "平行分析图": "Parallel Analysis Plot",
    "潜在剖面图": "Latent Profile Plot",
    "学习投入雷达图": "Learning Engagement Radar Chart",
    "竞争风险图": "Competing Risks Plot",
    "浓度—时间曲线": "Concentration–time Curve",
    "病例时间轴": "Case Timeline",
    "风险评分图": "Risk Score Plot",
    "富集条形图": "Enrichment Bar Chart",
    "单细胞轨迹图": "Single-cell Trajectory Plot",
    "集合桑基图": "Set Sankey Diagram",
    "交集条形图": "Intersection Bar Chart",
    "马赛克图": "Mosaic Plot",
    "关联图": "Association Plot",
    "三维等高线图": "Three-dimensional Contour Plot",
    "流体粒子轨迹图": "Fluid Particle Trajectory Plot",
    "庞加莱截面图": "Poincaré Section Plot",
    "混沌吸引子图": "Chaotic Attractor Plot",
    "极坐标图": "Polar Coordinate Plot",
    "球坐标图": "Spherical Coordinate Plot",
    "复平面图": "Complex Plane Plot",
    "等值线图": "Contour Plot",
    "热传导场图": "Heat Conduction Field Plot",
    "应力云图": "Stress Contour Plot",
    "位移云图": "Displacement Contour Plot",
    "电场分布图": "Electric Field Distribution Plot",
    "磁场分布图": "Magnetic Field Distribution Plot",
    "运行图": "Run Chart",
    "帕累托图": "Pareto Chart",
    "等高线优化图": "Contour Optimization Plot",
    "期刊发文量图": "Journal Publication Count Plot",
    "高被引文献排名图": "Highly Cited Publication Ranking Plot",
    "关键词时区图": "Keyword Time-zone Plot",
    "主题河流图": "Theme River",
    "合作弦图": "Collaboration Chord Diagram",
    "学科流动桑基图": "Discipline Flow Sankey Diagram",
    "时间切片网络图": "Time-slice Network",
    "引文年轮图": "Citation Tree-ring Plot",
    "聚类时间线视图": "Cluster Timeline View",
    "机制链条图": "Mechanism Chain Diagram",
    "跨层作用模型图": "Cross-level Effect Model Diagram",
    "神经网络结构图": "Neural Network Architecture Diagram",
    "研究阶段甘特图": "Research-stage Gantt Chart",
    "柱线组合图": "Bar and Line Composite Chart",
    "雨云图": "Raincloud Plot",
}


# 采用最长词组匹配；词典不命中时直接报错，避免静默生成无意义 ID。
TERM_TRANSLATIONS = {
    "三维矢量场图": "Three-dimensional Vector Field Plot",
    "百分比堆积柱状图": "100 Percent Stacked Bar Chart",
    "百分比堆积面积图": "100 Percent Stacked Area Chart",
    "系统动力学库存—流量图": "System Dynamics Stock and Flow Diagram",
    "验证性因素分析路径图": "Confirmatory Factor Analysis Path Diagram",
    "有调节的中介模型图": "Moderated Mediation Model Diagram",
    "结构方程模型路径图": "Structural Equation Model Path Diagram",
    "多层模型毛毛虫图": "Multilevel Model Caterpillar Plot",
    "认知诊断属性掌握图": "Cognitive Diagnosis Attribute Mastery Plot",
    "主题密度—中心度图": "Theme Density and Centrality Plot",
    "小提琴—箱线—散点组合图": "Violin Box and Scatter Composite Plot",
    "散点—边际密度组合图": "Scatter and Marginal Density Composite Plot",
    "热力图—聚类树组合图": "Heatmap and Dendrogram Composite Plot",
    "森林图—漏斗图组合": "Forest and Funnel Composite Figure",
    "地图—时间序列组合": "Map and Time-series Composite Figure",
    "地图—桑基图组合": "Map and Sankey Composite Figure",
    "网络图—时间线组合": "Network and Timeline Composite Figure",
    "主图—局部放大图": "Main Figure with Magnified Inset",
    "箱线—散点叠加图": "Box and Scatter Overlay Plot",
    "投入—过程—产出图": "Input Process Output Diagram",
    "Context–Mechanism–Outcome图": "Context Mechanism Outcome Diagram",
    "同比／环比变化图": "Year-on-year and Period-on-period Change Plot",
    "Gardner–Altman估计图": "Gardner–Altman Estimation Plot",
    "Cumming估计图": "Cumming Estimation Plot",
    "先验—后验比较图": "Prior and Posterior Comparison Plot",
    "概率校准带图": "Probability Calibration Band Plot",
    "统计显著性区间图": "Statistical Significance Interval Plot",
    "随机化检验分布图": "Randomization Test Distribution Plot",
    "多因素响应曲面图": "Multifactor Response Surface Plot",
    "正交设计效应图": "Orthogonal Design Effect Plot",
    "预测值—实际值图": "Predicted versus Observed Plot",
    "多分类ROC图": "Multiclass ROC Plot",
    "多分类PR图": "Multiclass Precision–Recall Plot",
    "模型公平性比较图": "Model Fairness Comparison Plot",
    "模型残差分布图": "Model Residual Distribution Plot",
    "随机森林树结构图": "Random Forest Tree Structure Diagram",
    "多层分类网络图": "Multilevel Classification Network",
    "网络时间演化图": "Temporal Network Evolution Plot",
    "网络中心性分布图": "Network Centrality Distribution Plot",
    "网络社区桑基图": "Network Community Sankey Diagram",
    "Alluvial网络演化图": "Alluvial Network Evolution Diagram",
    "状态迁移矩阵热力图": "State Transition Matrix Heatmap",
    "地理加权回归地图": "Geographically Weighted Regression Map",
    "双变量分级设色地图": "Bivariate Choropleth Map",
    "遥感假彩色图": "Remote-sensing False-color Image",
    "卫星影像叠加图": "Satellite Image Overlay",
    "Chernoff脸谱图": "Chernoff Faces Plot",
    "多维尺度气泡图": "Multidimensional Scaling Bubble Plot",
    "维度相关网络图": "Dimension Correlation Network",
    "文档—术语矩阵图": "Document–term Matrix Plot",
    "扎根理论范畴关系图": "Grounded Theory Category Relationship Diagram",
    "班级／学校增值图": "Class and School Value-added Plot",
    "学习行为时间序列图": "Learning Behavior Time-series Plot",
    "教师—学生关系网络图": "Teacher–student Relationship Network",
    "药代动力学曲线": "Pharmacokinetic Curve",
    "基因组浏览器轨迹图": "Genome Browser Track",
    "细胞通信网络图": "Cell Communication Network",
    "有限元网格图": "Finite Element Mesh Plot",
    "过程能力直方图": "Process Capability Histogram",
    "测量系统分析图": "Measurement System Analysis Plot",
    "知识基础聚类图": "Knowledge Base Cluster Plot",
    "研究前沿演化图": "Research Front Evolution Plot",
    "文献共被引聚类图": "Document Co-citation Cluster Plot",
    "引用生命周期图": "Citation Lifecycle Plot",
    "研究技术路线图": "Research Technical Roadmap",
    "研究问题映射图": "Research Question Mapping Diagram",
    "理论分析框架图": "Theoretical Analysis Framework",
    "证据综合流程图": "Evidence Synthesis Flow Diagram",
    "仪表板式科研图": "Research Dashboard Figure",
    "多模态可视化图": "Multimodal Visualization",
    "矩阵式综合图": "Matrix Composite Figure",
    "图表—表格组合": "Chart and Table Composite Figure",
    "累积发生函数图": "Cumulative Incidence Function Plot",
    "Kaplan–Meier生存曲线": "Kaplan–Meier Survival Curve",
    "Nelson–Aalen曲线": "Nelson–Aalen Curve",
    "三维": "Three-dimensional",
    "二维": "Two-dimensional",
    "多变量": "Multivariate",
    "高维": "High-dimensional",
    "多层": "Multilevel",
    "多因素": "Multifactor",
    "多分类": "Multiclass",
    "多模态": "Multimodal",
    "时间序列": "Time-series",
    "结构方程": "Structural Equation",
    "因果森林": "Causal Forest",
    "回归系数": "Regression Coefficient",
    "边际效应": "Marginal Effect",
    "交互效应": "Interaction Effect",
    "主效应": "Main Effect",
    "学校效应": "School Effect",
    "组间": "Between-group",
    "前后测": "Pretest–posttest",
    "重复测量": "Repeated-measures",
    "倾向得分": "Propensity Score",
    "主成分": "Principal Component",
    "模型残差": "Model Residual",
    "模型比较": "Model Comparison",
    "模型公平性": "Model Fairness",
    "交叉验证": "Cross-validation",
    "混淆矩阵": "Confusion Matrix",
    "协方差矩阵": "Covariance Matrix",
    "相关热力图": "Correlation Heatmap",
    "聚类热力图": "Clustered Heatmap",
    "区间热力图": "Interval Heatmap",
    "风险热力图": "Risk Heatmap",
    "知识掌握热力图": "Knowledge Mastery Heatmap",
    "基因表达热力图": "Gene Expression Heatmap",
    "网络矩阵热力图": "Network Matrix Heatmap",
    "重叠热力图": "Overlap Heatmap",
    "共词矩阵热力图": "Co-word Matrix Heatmap",
    "文本相似度热力图": "Text Similarity Heatmap",
    "箱线图": "Box Plot",
    "小提琴图": "Violin Plot",
    "森林图": "Forest Plot",
    "散点图": "Scatter Plot",
    "轨迹图": "Trajectory Plot",
    "曲面图": "Surface Plot",
    "控制图": "Control Chart",
    "流程图": "Flow Diagram",
    "路径图": "Path Diagram",
    "网络图": "Network",
    "地图": "Map",
    "热力图": "Heatmap",
    "矩阵": "Matrix",
    "时间线": "Timeline",
    "分布图": "Distribution Plot",
    "比较图": "Comparison Plot",
    "诊断图": "Diagnostic Plot",
    "效应图": "Effect Plot",
    "概率图": "Probability Plot",
    "得分图": "Score Plot",
    "载荷图": "Loading Plot",
    "拟合图": "Fit Plot",
    "树状图": "Dendrogram",
    "流程": "Flow",
    "框架": "Framework",
    "架构": "Architecture",
    "模型": "Model",
    "曲线": "Curve",
    "分布": "Distribution",
    "聚类": "Clustering",
    "关系": "Relationship",
    "相关": "Correlation",
    "演化": "Evolution",
    "协作": "Collaboration",
    "合作": "Collaboration",
    "共现": "Co-occurrence",
    "共被引": "Co-citation",
    "文献耦合": "Bibliographic Coupling",
    "引文": "Citation",
    "关键词": "Keyword",
    "主题": "Theme",
    "语义": "Semantic",
    "概念": "Concept",
    "证据": "Evidence",
    "因果": "Causal",
    "逻辑": "Logic",
    "理论": "Theoretical",
    "机制": "Mechanism",
    "研究": "Research",
    "实验": "Experiment",
    "设计": "Design",
    "方法": "Method",
    "数据": "Data",
    "处理": "Processing",
    "清洗": "Cleaning",
    "样本": "Sample",
    "筛选": "Screening",
    "阶段": "Stage",
    "步骤": "Step",
    "装置": "Apparatus",
    "算法": "Algorithm",
    "数据库": "Database",
    "系统": "System",
    "变量": "Variable",
    "编码": "Coding",
    "文献": "Literature",
    "混合": "Mixed",
    "整合": "Integration",
    "综合": "Synthesis",
    "报告": "Reporting",
    "技术": "Technical",
    "路线图": "Roadmap",
    "框架图": "Framework Diagram",
    "示意图": "Schematic",
    "结构图": "Structure Diagram",
    "组合图": "Composite Figure",
    "叠加图": "Overlay Plot",
    "表格": "Table",
    "局部": "Local",
    "放大": "Magnified",
    "学习": "Learning",
    "成绩": "Achievement",
    "投入": "Engagement",
    "行为": "Behavior",
    "路径": "Path",
    "学校": "School",
    "班级": "Class",
    "教师": "Teacher",
    "学生": "Student",
    "项目": "Item",
    "题目": "Item",
    "难度": "Difficulty",
    "信度": "Reliability",
    "测验": "Test",
    "测量": "Measurement",
    "不变性": "Invariance",
    "潜在": "Latent",
    "类别": "Class",
    "增长": "Growth",
    "调节": "Moderation",
    "中介": "Mediation",
    "能力": "Ability",
    "画像": "Profile",
    "课堂": "Classroom",
    "互动": "Interaction",
    "认知": "Cognitive",
    "诊断": "Diagnosis",
    "属性": "Attribute",
    "掌握": "Mastery",
    "生存": "Survival",
    "累积": "Cumulative",
    "风险": "Risk",
    "发生": "Incidence",
    "剂量": "Dose",
    "反应": "Response",
    "浓度": "Concentration",
    "药代动力学": "Pharmacokinetic",
    "生长": "Growth",
    "发病率": "Incidence",
    "热点": "Hotspot",
    "传播": "Transmission",
    "患者": "Patient",
    "病例": "Case",
    "生物标志物": "Biomarker",
    "肿瘤": "Tumor",
    "负荷": "Burden",
    "基因组": "Genome",
    "基因": "Gene",
    "表达": "Expression",
    "富集": "Enrichment",
    "细胞": "Cell",
    "通信": "Communication",
    "集合": "Set",
    "交集": "Intersection",
    "组合": "Combination",
    "重叠": "Overlap",
    "二元": "Binary",
    "交叉表": "Contingency Table",
    "四格表": "Two-by-two Table",
    "条件频率": "Conditional Frequency",
    "花瓣": "Petal",
    "韦恩": "Venn",
    "柱状图": "Bar Chart",
    "堆积": "Stacked",
    "面积图": "Area Chart",
    "圆环": "Circular",
    "层级": "Hierarchy",
    "图标": "Pictogram",
    "比例": "Proportion",
    "估计": "Estimation",
    "收敛": "Convergence",
    "后验": "Posterior",
    "先验": "Prior",
    "贝叶斯": "Bayesian",
    "山脊图": "Ridgeline Plot",
    "半眼图": "Half-eye Plot",
    "预测": "Prediction",
    "统计": "Statistical",
    "显著性": "Significance",
    "均值": "Mean",
    "个体": "Individual",
    "变化": "Change",
    "随机化": "Randomization",
    "检验": "Test",
    "非劣效性": "Non-inferiority",
    "一致性": "Agreement",
    "响应": "Response",
    "正交": "Orthogonal",
    "残差": "Residual",
    "标准化": "Standardized",
    "异方差": "Heteroscedasticity",
    "多重共线性": "Multicollinearity",
    "系数": "Coefficient",
    "实际值": "Observed Value",
    "偏差": "Bias",
    "方差": "Variance",
    "信息准则": "Information Criterion",
    "正则化": "Regularization",
    "空间": "Spatial",
    "置信区间": "Confidence Interval",
    "误差": "Error",
    "特征": "Feature",
    "重要性": "Importance",
    "规则": "Rule",
    "降维": "Dimensionality Reduction",
    "组织": "Organization",
    "分类": "Classification",
    "家谱": "Genealogy",
    "节点": "Node",
    "中心性": "Centrality",
    "度": "Degree",
    "社群": "Community",
    "状态": "State",
    "迁移": "Transition",
    "能量": "Energy",
    "物质": "Material",
    "流向": "Flow",
    "事件": "Event",
    "转化": "Conversion",
    "转移": "Transition",
    "概率": "Probability",
    "地理": "Geographic",
    "加权": "Weighted",
    "回归": "Regression",
    "双变量": "Bivariate",
    "分级设色": "Choropleth",
    "三变量": "Trivariate",
    "地形": "Terrain",
    "遥感": "Remote Sensing",
    "假彩色": "False Color",
    "土地利用": "Land Use",
    "卫星影像": "Satellite Imagery",
    "可达性": "Accessibility",
    "脸谱": "Faces",
    "因子": "Factor",
    "自组织映射": "Self-organizing Map",
    "尺度": "Scaling",
    "气泡图": "Bubble Plot",
    "四元": "Quaternary",
    "协调图": "Co-plot",
    "词频": "Word Frequency",
    "共词": "Co-word",
    "情感": "Sentiment",
    "极性": "Polarity",
    "文本": "Text",
    "文档": "Document",
    "术语": "Term",
    "频次": "Frequency",
    "质性": "Qualitative",
    "叙事": "Narrative",
    "案例": "Case",
    "话语": "Discourse",
    "差异": "Difference",
    "话题": "Topic",
    "扎根理论": "Grounded Theory",
    "范畴": "Category",
    "项目地图": "Item Map",
    "项目拟合": "Item Fit",
    "项目难度": "Item Difficulty",
    "效应": "Effect",
    "发生函数": "Incidence Function",
    "基因组浏览器": "Genome Browser",
    "轨迹": "Track",
    "系统发育": "Phylogenetic",
    "圆图": "Diagram",
    "控制": "Control",
    "过程能力": "Process Capability",
    "优化": "Optimization",
    "可靠性": "Reliability",
    "寿命": "Lifetime",
    "浴盆": "Bathtub",
    "年度": "Annual",
    "发文": "Publication",
    "趋势": "Trend",
    "期刊": "Journal",
    "高被引": "Highly Cited",
    "聚类时间线": "Cluster Timeline",
    "研究前沿": "Research Front",
    "生命周期": "Lifecycle",
    "假设": "Hypothesis",
    "跨层": "Cross-level",
    "问题树": "Problem Tree",
    "目标树": "Objective Tree",
    "逻辑树": "Logic Tree",
    "概念机制": "Conceptual Mechanism",
    "图": "Plot",
    "树": "Tree",
}


def parse_source(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    headings: list[str] = []
    entries: list[dict[str, str]] = []
    category_id: str | None = None
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("# "):
            if len(headings) < 24:
                headings.append(line[2:].strip())
                category_id = f"{len(headings):02d}"
            else:
                category_id = None
            continue
        match = re.match(r"^(\d+)\.\s+(.+?)\s*$", line)
        if category_id and match:
            entries.append(
                {
                    "category_id": category_id,
                    "ordinal": match.group(1),
                    "source_label": match.group(2),
                    "line": str(line_number),
                }
            )
    if len(headings) != 24:
        raise ValueError(f"Expected 24 source headings, found {len(headings)}")
    if len(entries) != 714:
        raise ValueError(f"Expected 714 source memberships, found {len(entries)}")
    return headings, entries


def split_label(label: str) -> tuple[str, str | None, list[str]]:
    match = re.match(r"^(.*?)（(.*?)）$", label)
    if not match:
        return label.strip(), None, []
    name_zh = match.group(1).strip()
    raw_en = match.group(2).strip()
    if not re.search(r"[A-Za-z]", raw_en):
        return name_zh, None, []
    parts = [part.strip() for part in re.split(r"[／/]", raw_en) if part.strip()]
    primary = parts[0]
    aliases = parts[1:]
    if aliases:
        suffix_match = re.search(r"\b(Chart|Plot|Diagram|Map|Curve|Graph|Matrix|Network)$", aliases[0])
        if suffix_match and not re.search(
            r"\b(Chart|Plot|Diagram|Map|Curve|Graph|Matrix|Network)$", primary
        ):
            primary = f"{primary} {suffix_match.group(1)}"
    if "," in primary:
        primary, abbreviation = [part.strip() for part in primary.split(",", 1)]
        aliases.append(abbreviation)
    return name_zh, primary, aliases


def translate_chinese_name(name_zh: str) -> str:
    if name_zh in FULL_ENGLISH_NAMES:
        return FULL_ENGLISH_NAMES[name_zh]
    terms = sorted(TERM_TRANSLATIONS, key=len, reverse=True)
    words: list[str] = []
    index = 0
    while index < len(name_zh):
        ascii_match = re.match(r"[A-Za-z0-9%&+./-]+", name_zh[index:])
        if ascii_match:
            words.append(ascii_match.group(0))
            index += len(ascii_match.group(0))
            continue
        if name_zh[index] in "—–－／/（）()、· ":
            index += 1
            continue
        for term in terms:
            if name_zh.startswith(term, index):
                words.append(TERM_TRANSLATIONS[term])
                index += len(term)
                break
        else:
            raise ValueError(
                f"Missing English translation at {name_zh!r}, offset {index}: {name_zh[index:]!r}"
            )
    return " ".join(words)


def slugify(value: str) -> str:
    value = value.casefold().replace("100%", "100-percent").replace("%", "percent")
    value = value.replace("&", " and ").replace("3d", "three-dimensional")
    value = re.sub(r"[’'`]", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    if not value:
        raise ValueError(f"Cannot derive canonical ID from {value!r}")
    return value


def source_variants(label: str) -> tuple[str, str | None, list[str]]:
    name_zh, name_en, aliases_en = split_label(label)
    return name_zh, name_en, aliases_en


def current_lookup(charts: list[dict[str, Any]]) -> dict[str, set[str]]:
    lookup: dict[str, set[str]] = defaultdict(set)
    for chart in charts:
        for value in [
            chart["id"],
            chart["name_zh"],
            chart["name_en"],
            *chart["aliases_zh"],
            *chart["aliases_en"],
        ]:
            lookup[normalize_alias(value)].add(chart["id"])
    return lookup


def remap_existing_chart(chart: dict[str, Any], remap_categories: bool) -> dict[str, Any]:
    chart = deepcopy(chart)
    if remap_categories:
        mapped = list(dict.fromkeys(OLD_CATEGORY_REMAP[item] for item in chart["category_ids"]))
        chart["category_ids"] = mapped
        chart["primary_category_id"] = OLD_CATEGORY_REMAP[chart["primary_category_id"]]
    chart["source_memberships"] = []
    chart["registry_origin"] = "repository_extension"
    return chart


def merge_existing_charts(charts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {chart["id"]: chart for chart in charts}
    for old_id, target_id in MERGE_EXISTING_IDS.items():
        if old_id not in by_id:
            continue
        old = by_id.pop(old_id)
        target = by_id[target_id]
        for value in [old["name_zh"], *old["aliases_zh"]]:
            if value != target["name_zh"] and value not in target["aliases_zh"]:
                target["aliases_zh"].append(value)
        for value in [old["name_en"], *old["aliases_en"]]:
            if value != target["name_en"] and value not in target["aliases_en"]:
                target["aliases_en"].append(value)
        target["category_ids"] = sorted(set(target["category_ids"] + old["category_ids"]))
        for chart in by_id.values():
            for field in ("alternatives", "complements", "components"):
                chart[field] = [target_id if item == old_id else item for item in chart[field]]
                chart[field] = list(dict.fromkeys(chart[field]))
    return list(by_id.values())


def build_new_chart(chart_id: str, name_zh: str, name_en: str, category_id: str) -> dict[str, Any]:
    profile = CATEGORY_PROFILES[category_id]
    specialized = category_id in {"09", "10", "11", "12", "13", "14", "15", "16", "17", "19", "20", "21", "22", "23", "24"}
    return {
        "id": chart_id,
        "name_zh": name_zh,
        "name_en": name_en,
        "aliases_zh": [],
        "aliases_en": [],
        "category_ids": [category_id],
        "primary_category_id": category_id,
        "information_tasks": [profile["task"]],
        "disciplines": profile["disciplines"],
        "definition": f"{name_zh}用于{profile['task']}，其视觉编码和统计解释必须与数据契约一致。",
        "research_questions": [f"如何用{name_zh}可靠回答“{profile['task']}”这一研究问题？"],
        "observation_unit": profile["unit"],
        "required_variables": profile["required"],
        "optional_variables": profile["optional"],
        "data_types": profile["types"],
        "minimum_sample": "由研究设计、估计稳定性与目标结论共同决定；小样本应保留个体证据。",
        "suitable_when": [f"数据结构能够支持{profile['task']}", "视觉编码与研究问题和统计方法一致"],
        "avoid_when": ["缺少图型必需变量或领域对象", "仅因外形相似而替代语义不同的专业图"],
        "visual_encoding": profile["encoding"],
        "statistics": ["明确图中统计量、模型输出或聚合量的定义"],
        "uncertainty": ["有推断性结论时报告与研究设计匹配的不确定性"],
        "allowed_transforms": ["仅使用预先声明、可复现且不改变结论含义的数据变换"],
        "forbidden_transforms": ["为强化视觉信号而修改数值", "未披露的筛选、截断、平滑或重排"],
        "axes_scales": ["单位、尺度、坐标系和变换必须在轴或图注中说明"],
        "color_grayscale": ["使用感知合理、色盲安全并可灰度辨识的配色"],
        "accessibility": ["关键结论使用位置、形状、线型、标签或顺序进行冗余编码"],
        "annotations": ["只标注支持核心结论所需的对象、阈值、事件和统计信息"],
        "publication_risks": [
            "数据契约、统计方法或样本量披露不足",
            "使用装饰性编码、误导尺度或把描述性结构写成因果结论",
        ],
        "implementation_status": "on_demand" if specialized else profile["status"],
        "backends": [],
        "dependencies": [],
        "asset_path": None,
        "reuse_constraints": ["必须根据真实数据、终稿尺寸和目标期刊重新实现并完成四轮 QA"],
        "alternatives": ["dot-plot"],
        "complements": ["interval-plot"],
        "qa_rules": ["检查数据契约、尺度、颜色、标注、可访问性和导出文件"],
        "source_memberships": [],
        "components": [],
        "registry_origin": "source_taxonomy",
    }


def resolve_or_create(
    charts_by_id: dict[str, dict[str, Any]],
    lookup: dict[str, set[str]],
    entry: dict[str, str],
) -> tuple[dict[str, Any], list[str]]:
    category_id = entry["category_id"]
    source_label = entry["source_label"]
    name_zh, supplied_name_en, supplied_aliases_en = source_variants(source_label)
    override = ENTRY_ID_OVERRIDES.get((category_id, name_zh)) or LABEL_ID_OVERRIDES.get(name_zh)

    keys = [normalize_alias(source_label), normalize_alias(name_zh)]
    if supplied_name_en:
        keys.append(normalize_alias(supplied_name_en))
    candidates = set().union(*(lookup.get(key, set()) for key in keys))
    if override:
        chart_id = override
    elif len(candidates) == 1:
        chart_id = next(iter(candidates))
    elif len(candidates) > 1:
        raise ValueError(f"Unresolved alias ambiguity for {category_id} {source_label!r}: {sorted(candidates)}")
    else:
        name_en = supplied_name_en or translate_chinese_name(name_zh)
        chart_id = slugify(name_en)

    if chart_id not in charts_by_id:
        canonical_names = ENTRY_CANONICAL_NAMES.get((category_id, source_label))
        if canonical_names is None:
            canonical_names = (
                name_zh,
                supplied_name_en or translate_chinese_name(name_zh),
            )
        canonical_name_zh, canonical_name_en = canonical_names
        charts_by_id[chart_id] = build_new_chart(
            chart_id, canonical_name_zh, canonical_name_en, category_id
        )
    chart = charts_by_id[chart_id]
    if override and chart_id not in charts_by_id:
        raise ValueError(f"Override points to an unknown chart: {chart_id}")

    if name_zh != chart["name_zh"] and name_zh not in chart["aliases_zh"]:
        chart["aliases_zh"].append(name_zh)
    if supplied_name_en and supplied_name_en != chart["name_en"] and supplied_name_en not in chart["aliases_en"]:
        chart["aliases_en"].append(supplied_name_en)
    for alias in supplied_aliases_en:
        if alias != chart["name_en"] and alias not in chart["aliases_en"]:
            chart["aliases_en"].append(alias)
    if category_id not in chart["category_ids"]:
        chart["category_ids"].append(category_id)
    chart["source_memberships"].append(
        {"source_category_id": category_id, "source_label": source_label}
    )
    chart["registry_origin"] = "source_taxonomy"

    for value in [source_label, name_zh, supplied_name_en, *supplied_aliases_en]:
        if value:
            lookup[normalize_alias(value)].add(chart_id)
    return chart, supplied_aliases_en


def render_source(headings: list[str], entries: list[dict[str, str]], assignments: list[str]) -> str:
    category_names = {category_id: name_zh for category_id, _, name_zh, _ in CATEGORIES}
    grouped: dict[str, list[tuple[dict[str, str], str]]] = defaultdict(list)
    for entry, chart_id in zip(entries, assignments, strict=True):
        grouped[entry["category_id"]].append((entry, chart_id))
    lines = [
        "# 科研数据可视化图表源分类",
        "",
        "> 本文件保存用户提供的 24 类、714 条原始分类归属，并为每条源记录附加 canonical ID。",
        "> 原始重复项作为分类归属保留，但规范定义只在 `chart-registry.yaml` 中保存一次。",
        "",
    ]
    for index, heading in enumerate(headings, start=1):
        category_id = f"{index:02d}"
        lines.extend([f"## {category_id}. {category_names[category_id]}", ""])
        for entry, chart_id in grouped[category_id]:
            lines.append(
                f"- `{chart_id}` — {entry['source_label']} "
                f"<!-- source:{category_id}:{entry['ordinal']} -->"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def load_base_registry(revision: str | None) -> dict[str, Any]:
    if revision is None:
        return load_registry()
    completed = subprocess.run(
        ["git", "show", f"{revision}:references/chart-registry.yaml"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(completed.stdout)


def import_taxonomy(source_path: Path, base_revision: str | None = None) -> dict[str, Any]:
    headings, entries = parse_source(source_path)
    registry = load_base_registry(base_revision)
    expected_slugs = [slug for _, slug, _, _ in CATEGORIES]
    current_slugs = [category["slug"] for category in registry["categories"]]
    remap_categories = current_slugs != expected_slugs
    charts = merge_existing_charts(
        [
            remap_existing_chart(chart, remap_categories=remap_categories)
            for chart in registry["charts"]
        ]
    )
    charts_by_id = {chart["id"]: chart for chart in charts}
    lookup = current_lookup(charts)
    assignments: list[str] = []

    for entry in entries:
        chart, _ = resolve_or_create(charts_by_id, lookup, entry)
        assignments.append(chart["id"])

    for chart in charts_by_id.values():
        chart["category_ids"] = sorted(set(chart["category_ids"]))
        if chart["source_memberships"]:
            chart["primary_category_id"] = chart["source_memberships"][0]["source_category_id"]
        elif chart["primary_category_id"] not in chart["category_ids"]:
            chart["primary_category_id"] = chart["category_ids"][0]
        chart["aliases_zh"] = sorted(set(chart["aliases_zh"]), key=normalize_alias)
        chart["aliases_en"] = sorted(set(chart["aliases_en"]), key=normalize_alias)

    registry["registry_version"] = "2.1.0"
    registry["generated_at"] = None
    registry["source_expectation"] = {
        "declared_memberships": 714,
        "available_source_memberships": 714,
        "source_complete": True,
        "note": "The supplied 24-category source taxonomy is present and all 714 memberships are mapped.",
    }
    registry["categories"] = [
        {"id": category_id, "slug": slug, "name_zh": name_zh, "name_en": name_en}
        for category_id, slug, name_zh, name_en in CATEGORIES
    ]
    registry["charts"] = sorted(charts_by_id.values(), key=lambda chart: chart["id"])
    registry["ambiguous_terms"] = [
        {
            "term": "漏斗图",
            "candidate_ids": ["meta-analysis-funnel-plot", "conversion-funnel-chart"],
            "resolution": "统计估计或医学证据综合使用 meta-analysis-funnel-plot；流程转化使用 conversion-funnel-chart。",
        },
        {
            "term": "棒棒糖图",
            "candidate_ids": ["lollipop-chart", "mutation-lollipop-plot"],
            "resolution": "通用类别排序使用 lollipop-chart；基因突变位点使用 mutation-lollipop-plot。",
        },
        {
            "term": "瀑布图",
            "candidate_ids": ["contribution-waterfall-chart", "tumor-response-waterfall-plot"],
            "resolution": "一般增减贡献使用 contribution-waterfall-chart；肿瘤疗效使用 tumor-response-waterfall-plot。",
        },
        {
            "term": "蜘蛛图",
            "candidate_ids": ["radar-chart", "tumor-burden-spider-plot"],
            "resolution": "多指标画像使用 radar-chart；肿瘤负荷随时间变化使用 tumor-burden-spider-plot。",
        },
    ]
    canonical_alias_owners: dict[str, str] = {}
    for chart in registry["charts"]:
        canonical_alias_owners[normalize_alias(chart["name_zh"])] = chart["id"]
        canonical_alias_owners[normalize_alias(chart["name_en"])] = chart["id"]
    ambiguous_keys = {normalize_alias(item["term"]) for item in registry["ambiguous_terms"]}
    for chart in registry["charts"]:
        chart["aliases_zh"] = [
            alias for alias in chart["aliases_zh"]
            if canonical_alias_owners.get(normalize_alias(alias), chart["id"]) == chart["id"]
            or normalize_alias(alias) in ambiguous_keys
        ]
        chart["aliases_en"] = [
            alias for alias in chart["aliases_en"]
            if canonical_alias_owners.get(normalize_alias(alias), chart["id"]) == chart["id"]
            or normalize_alias(alias) in ambiguous_keys
        ]
    return {
        "registry": registry,
        "source": render_source(headings, entries, assignments),
        "memberships": len(entries),
        "canonical_charts": len(registry["charts"]),
        "source_charts": sum(chart["registry_origin"] == "source_taxonomy" for chart in registry["charts"]),
        "extensions": sum(chart["registry_origin"] == "repository_extension" for chart in registry["charts"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="UTF-8 Markdown/text file containing the 24 categories")
    parser.add_argument(
        "--base-revision",
        help="Read the pre-import registry from a Git revision, useful when repeating a migration",
    )
    parser.add_argument("--check", action="store_true", help="Validate importability without writing files")
    args = parser.parse_args()
    result = import_taxonomy(args.source, args.base_revision)
    if not args.check:
        REGISTRY_PATH.write_text(
            json.dumps(result["registry"], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        SOURCE_PATH.write_text(result["source"], encoding="utf-8")
    action = "validated" if args.check else "imported"
    print(
        f"Source taxonomy {action}: {result['memberships']} memberships, "
        f"{result['canonical_charts']} canonical charts "
        f"({result['source_charts']} source, {result['extensions']} repository extensions)"
    )


if __name__ == "__main__":
    main()
