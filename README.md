<p align="center">
  <img src="assets/readme/academic-data-visualization-workflow-v5.png" width="100%" alt="从研究问题和数据剖析到投稿级成图与视觉复核的工作流">
</p>

<p align="center">
  <strong>科研问题 → 数据契约 → 图型论证 → 投稿级成图</strong><br>
  <sub>把真实数据与期刊约束转化为可复现、可审查、可投稿的 Python / R 科研图表。</sub>
</p>

<p align="center">
  <a href="references/figure-type-catalog.md"><img src="https://img.shields.io/badge/Taxonomy-24_categories-4573B4?style=flat-square" alt="24 类图型体系"></a>
  <a href="#能力范围"><img src="https://img.shields.io/badge/Source_memberships-714%2F714-73C79E?style=flat-square" alt="714/714 条源分类归属已映射"></a>
  <a href="references/directory-map.md"><img src="https://img.shields.io/badge/Production_assets-34_verified-F2A65A?style=flat-square" alt="34 类已核验生产资产"></a>
  <a href="#质量证据"><img src="https://img.shields.io/badge/QA-4_passes-95AEDA?style=flat-square" alt="四轮 QA"></a>
  <a href="https://github.com/Starry-cz/academic-data-visualization/actions/workflows/quality.yml"><img src="https://github.com/Starry-cz/academic-data-visualization/actions/workflows/quality.yml/badge.svg" alt="自动质量检查"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0-7A939F?style=flat-square" alt="Apache-2.0 License"></a>
</p>

<p align="center">
  <a href="#30-秒开始">快速开始</a> ·
  <a href="#为什么使用它">核心价值</a> ·
  <a href="#能力范围">能力范围</a> ·
  <a href="#精选成图">精选成图</a> ·
  <a href="#文档导航">文档导航</a> ·
  <a href="#质量证据">质量证据</a> ·
  <a href="README_EN.md">English</a>
</p>

> 这不是一个把数据硬塞进模板的图库。它先确认研究结论、观测单位、变量结构与投稿规格，再完成选图、资产复用或按需实现，并对最终尺寸的 RGB 与灰度结果做四轮 QA。

## 30 秒开始

安装完整 Skill，而不是只复制 `SKILL.md`：

```powershell
# Windows PowerShell · Codex
git clone https://github.com/Starry-cz/academic-data-visualization.git "$env:USERPROFILE\.codex\skills\academic-data-visualization"
```

```bash
# macOS / Linux · Codex
git clone https://github.com/Starry-cz/academic-data-visualization.git ~/.codex/skills/academic-data-visualization
```

然后直接描述研究问题、数据与交付规格：

```text
使用 academic-data-visualization 分析 experiment.csv。
我要比较三种处理在四个时间点的变化。请先检查样本量、分布、缺失值和重复测量结构，
再论证图型与多面板方案；目标是双栏论文主图，交付可编辑矢量文件、450 dpi 校样、
灰度校样和 QA 报告。
```

## 为什么使用它

<table width="100%" align="center">
  <tr>
    <th width="25%">结论驱动</th>
    <th width="25%">真实能力边界</th>
    <th width="25%">可复用生产资产</th>
    <th width="25%">投稿前闭环</th>
  </tr>
  <tr>
    <td width="25%"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt="">先判断读者需要比较、关联还是决策，再选择图型</td>
    <td width="25%">665 个规范化图型均标记真实实现状态，不把“已登记”冒充“已有模板”</td>
    <td width="25%">34 类资产具备脚本、预览和 manifest，可追溯复用</td>
    <td width="25%">同时检查反模式、代码与导出、科学逻辑、最终渲染</td>
  </tr>
</table>

传统绘图请求常从“画柱状图/热图”开始；本 Skill 从研究主张和数据契约开始，并主动拦截小样本均值柱、双 Y 轴、彩虹色图、错误连线、误导性截轴等常见风险。

## 它如何工作

<table width="100%" align="center">
  <tr><th width="20%">阶段</th><th width="60%">关键动作</th><th width="20%">产出</th></tr>
  <tr><td width="20%"><strong>1. 定义</strong></td><td width="60%"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt="">明确结论、观测单位、变量、依赖结构和目标期刊</td><td width="20%"><a href="references/figure-contract.md">图表契约</a></td></tr>
  <tr><td width="20%"><strong>2. 论证</strong></td><td width="60%">剖析样本量、分布、缺失、异常值与分组，比较候选图型</td><td width="20%">图型理由与风险</td></tr>
  <tr><td width="20%"><strong>3. 实现</strong></td><td width="60%">路由生产模板、可复用模式或按需实现，统一面板与配色</td><td width="20%">Python / R 与矢量主文件</td></tr>
  <tr><td width="20%"><strong>4. 验证</strong></td><td width="60%">程序检查、最终尺寸 RGB 复核、灰度复核和导出审查</td><td width="20%">校样与 QA 报告</td></tr>
</table>

## 能力范围

<!-- chart-registry:summary:start -->
注册表严格区分目录覆盖与实现状态；只有生产模板拥有可复用脚本、预览和 manifest。

<table width="100%" align="center">
  <tr><td width="50%"><strong>分类体系</strong></td><td width="50%"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt="">24 类</td></tr>
  <tr><td width="50%"><strong>规范化图型</strong></td><td width="50%">665 个</td></tr>
  <tr><td width="50%"><strong>源清单图型</strong></td><td width="50%">625 个</td></tr>
  <tr><td width="50%"><strong>仓库扩展图型</strong></td><td width="50%">40 个</td></tr>
  <tr><td width="50%"><strong>源分类归属</strong></td><td width="50%">714 / 714 条已映射</td></tr>
  <tr><td width="50%"><strong>生产模板</strong></td><td width="50%">34 类</td></tr>
  <tr><td width="50%"><strong>可复用模式</strong></td><td width="50%">228 类</td></tr>
  <tr><td width="50%"><strong>按需实现</strong></td><td width="50%">403 类</td></tr>
</table>
<!-- chart-registry:summary:end -->

<table width="100%" align="center">
  <tr><th width="25%">状态</th><th width="25%">含义</th><th width="50%">仓库承诺</th></tr>
  <tr><td width="25%"><code>production_template</code></td><td width="25%">已核验生产模板</td><td width="50%"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt="">真实脚本 + PNG + <code>asset.yaml</code>，可用时附 SVG/PDF</td></tr>
  <tr><td width="25%"><code>reusable_pattern</code></td><td width="25%">可复用实现模式</td><td width="50%">有明确数据契约与后端路由，但不声称已有独立资产</td></tr>
  <tr><td width="25%"><code>on_demand</code></td><td width="25%">按数据与依赖实现</td><td width="50%">不伪造预览，不用外形相似的普通图代替专业图型</td></tr>
</table>

查看 [24 类完整图型目录](references/figure-type-catalog.md)、[中英文别名索引](references/chart-alias-index.md)、[覆盖审计](references/chart-coverage-audit.md) 和 [真实生产资产映射](references/directory-map.md)。

## 精选成图

首页按画幅展示 22 个不同类型的真实案例；统一缩略图画布确保每一行左右对齐，点击图片可查看原始成图。完整实现状态请进入 [生产资产目录](assets/figures/) 与 [图型目录](references/figure-type-catalog.md)。

### 关系、降维、诊断与高维结构 · 3 × 4

<table width="100%" align="center">
  <tr>
    <td width="33%" align="center" valign="top"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt=""><strong>3D 热图</strong><br><a href="assets/figure-atlas/3Dheatmap.png"><img src="assets/figure-atlas/readme-cards/3Dheatmap.png" width="280" alt="3D 热图"></a><br><sub>高维强度结构</sub></td>
    <td width="34%" align="center" valign="top"><strong>密度热图</strong><br><a href="assets/figure-atlas/density_heatmap.png"><img src="assets/figure-atlas/readme-cards/density_heatmap.png" width="280" alt="密度热图"></a><br><sub>二维密度与聚集区</sub></td>
    <td width="33%" align="center" valign="top"><strong>PCA 双标图</strong><br><a href="assets/figure-atlas/PCA.png"><img src="assets/figure-atlas/readme-cards/PCA.png" width="280" alt="PCA 双标图"></a><br><sub>样本分离与载荷</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><strong>AUROC</strong><br><a href="assets/figure-atlas/auroc.png"><img src="assets/figure-atlas/readme-cards/auroc.png" width="280" alt="AUROC 曲线"></a><br><sub>模型判别能力</sub></td>
    <td width="34%" align="center" valign="top"><strong>相关密度图</strong><br><a href="assets/figure-atlas/CorrelationDensity.png"><img src="assets/figure-atlas/readme-cards/CorrelationDensity.png" width="280" alt="相关密度图"></a><br><sub>关系与局部密度</sub></td>
    <td width="33%" align="center" valign="top"><strong>相关矩阵</strong><br><a href="assets/figure-atlas/Correlationmatrix.png"><img src="assets/figure-atlas/readme-cards/Correlationmatrix.png" width="280" alt="相关矩阵"></a><br><sub>多变量关系</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><strong>分组相关矩阵</strong><br><a href="assets/figure-atlas/GroupCorrelationmatrix.png"><img src="assets/figure-atlas/readme-cards/GroupCorrelationmatrix.png" width="280" alt="分组相关矩阵"></a><br><sub>条件间相关结构</sub></td>
    <td width="34%" align="center" valign="top"><strong>雷达图</strong><br><a href="assets/figure-atlas/radar.png"><img src="assets/figure-atlas/readme-cards/radar.png" width="280" alt="雷达图"></a><br><sub>少量对象多指标</sub></td>
    <td width="33%" align="center" valign="top"><strong>山脊图</strong><br><a href="assets/figure-atlas/RidgePlot.png"><img src="assets/figure-atlas/readme-cards/RidgePlot.png" width="280" alt="山脊图"></a><br><sub>多组分布迁移</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><strong>气泡散点图</strong><br><a href="assets/figures/BubbleScatter/bubble_scatter.png"><img src="assets/figure-atlas/readme-cards/bubble_scatter.png" width="280" alt="气泡散点图"></a><br><sub>二维关系与第三变量</sub></td>
    <td width="34%" align="center" valign="top"><strong>相关气泡矩阵</strong><br><a href="assets/figures/CorrelationBubbleMatrix/correlation_bubble_matrix.png"><img src="assets/figure-atlas/readme-cards/correlation_bubble_matrix.png" width="280" alt="相关气泡矩阵"></a><br><sub>方向、强度与显著性</sub></td>
    <td width="33%" align="center" valign="top"><strong>相关网络图</strong><br><a href="assets/figures/CorrelationNetwork/correlation_network.png"><img src="assets/figure-atlas/readme-cards/correlation_network.png" width="280" alt="相关网络图"></a><br><sub>节点关系与社群结构</sub></td>
  </tr>
</table>

### 比较、分布、趋势、组成与空间 · 2 × 5

<table width="100%" align="center">
  <tr>
    <td width="50%" align="center" valign="top"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt=""><strong>柱状图</strong><br><a href="assets/figure-atlas/bar.png"><img src="assets/figure-atlas/readme-cards/bar.png" width="390" alt="柱状图"></a><br><sub>组间摘要与原始观测</sub></td>
    <td width="50%" align="center" valign="top"><strong>分组柱状图</strong><br><a href="assets/figure-atlas/GroupedBarChart.png"><img src="assets/figure-atlas/readme-cards/GroupedBarChart.png" width="390" alt="分组柱状图"></a><br><sub>多处理 × 多指标</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Mantel 关联图</strong><br><a href="assets/figure-atlas/MantelCorrelation.png"><img src="assets/figure-atlas/readme-cards/MantelCorrelation.png" width="390" alt="Mantel 关联图"></a><br><sub>距离矩阵与环境关联</sub></td>
    <td width="50%" align="center" valign="top"><strong>小提琴图</strong><br><a href="assets/figure-atlas/violin_chart.png"><img src="assets/figure-atlas/readme-cards/violin_chart.png" width="390" alt="小提琴图"></a><br><sub>分布形态与异常值</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>时间趋势</strong><br><a href="assets/figure-atlas/trend.png"><img src="assets/figure-atlas/readme-cards/trend.png" width="390" alt="时间趋势图"></a><br><sub>变化轨迹与不确定性</sub></td>
    <td width="50%" align="center" valign="top"><strong>堆叠柱状散点图</strong><br><a href="assets/figure-atlas/StackedBarScatter.png"><img src="assets/figure-atlas/readme-cards/StackedBarScatter.png" width="390" alt="堆叠柱状散点图"></a><br><sub>组成与样本级观测</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>频率 3D 热图</strong><br><a href="assets/figure-atlas/Frequency_3DHeatmap.png"><img src="assets/figure-atlas/readme-cards/Frequency_3DHeatmap.png" width="390" alt="频率 3D 热图"></a><br><sub>双因子分箱频次</sub></td>
    <td width="50%" align="center" valign="top"><strong>桑基图</strong><br><a href="assets/figure-atlas/sankey.png"><img src="assets/figure-atlas/readme-cards/sankey.png" width="390" alt="桑基图"></a><br><sub>类别流向与状态转换</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>堆叠面积图</strong><br><a href="assets/figures/StackedArea/stacked_area.png"><img src="assets/figure-atlas/readme-cards/stacked_area.png" width="390" alt="堆叠面积图"></a><br><sub>组成随时间变化</sub></td>
    <td width="50%" align="center" valign="top"><strong>地理气泡地图</strong><br><a href="assets/figures/GeographicBubbleMap/geographic_bubble_map.png"><img src="assets/figure-atlas/readme-cards/geographic_bubble_map.png" width="390" alt="地理气泡地图"></a><br><sub>空间位置与规模编码</sub></td>
  </tr>
</table>

## 配色系统

23 套主题覆盖分类、顺序和发散语义；默认要求色盲友好、灰度可辨、语义稳定，并支持从参考图片提取候选颜色后重新审查。

<table width="100%" align="center">
  <tr>
    <td width="50%" align="center" valign="top"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt=""><strong>Nature default</strong><br><img src="assets/palette-gallery/nature-default.png" width="390" alt="Nature default 配色预览"></td>
    <td width="50%" align="center" valign="top"><strong>Blue–red signal</strong><br><img src="assets/palette-gallery/blue-red-signal.png" width="390" alt="Blue-red signal 配色预览"></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Pastel harmony</strong><br><img src="assets/palette-gallery/pastel-harmony.png" width="390" alt="Pastel harmony 配色预览"></td>
    <td width="50%" align="center" valign="top"><strong>Coastal sunset</strong><br><img src="assets/palette-gallery/coastal-sunset.png" width="390" alt="Coastal sunset 配色预览"></td>
  </tr>
</table>

完整色值、语义角色与使用限制见 [`color-palettes.md`](references/color-palettes.md) 和 [`palette-library.json`](references/palette-library.json)。

## 适用边界

<table width="100%" align="center">
  <tr><th width="50%">适合</th><th width="50%">不适合</th></tr>
  <tr><td width="50%"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt="">论文主图、补充图、学位论文和科研报告</td><td width="50%">交互式仪表盘或 Web 数据产品</td></tr>
  <tr><td width="50%">不确定该选什么图，需要基于数据结构论证</td><td width="50%">没有定量面板的纯插画式机制图</td></tr>
  <tr><td width="50%">重绘旧图、统一多面板语言、适配目标期刊</td><td width="50%">与绘图无关的统计分析、清洗或文献综述</td></tr>
  <tr><td width="50%">投稿前检查裁切、遮挡、灰度、误导编码和导出</td><td width="50%">要求用普通图假装地图、基因组轨道或三维体数据</td></tr>
</table>

## 文档导航

<table width="100%" align="center">
  <tr><th width="50%">你要解决的问题</th><th width="50%">入口</th></tr>
  <tr><td width="50%">查找图型、别名与真实实现状态</td><td width="50%"><img src="assets/readme/table-full-width-spacer.svg" width="800" height="1" align="right" alt=""><a href="references/figure-type-catalog.md">图型目录</a> · <a href="references/chart-alias-index.md">别名索引</a> · <a href="references/chart-registry.yaml">注册表</a></td></tr>
  <tr><td width="50%">定义输入、结论与交付规格</td><td width="50%"><a href="references/figure-contract.md">图表契约</a> · <a href="references/figure-design-brief.md">设计简报</a></td></tr>
  <tr><td width="50%">组织多面板与视觉层级</td><td width="50%"><a href="references/multipanel-layout.md">多面板布局</a> · <a href="references/visual-style.md">视觉样式</a></td></tr>
  <tr><td width="50%">适配期刊尺寸与导出</td><td width="50%"><a href="references/journal-intel.md">期刊情报</a> · <a href="references/journal-specs.md">期刊规格</a> · <a href="references/export-specs.md">导出规格</a></td></tr>
  <tr><td width="50%">选择或扩展配色</td><td width="50%"><a href="references/color-palettes.md">配色指南</a> · <a href="references/palette-library.json">配色注册表</a></td></tr>
  <tr><td width="50%">复用资产并完成投稿前检查</td><td width="50%"><a href="references/asset-reuse-protocol.md">资产复用协议</a> · <a href="references/checklist.md">四轮 QA 清单</a></td></tr>
</table>

## 更多安装方式

完整仓库中的 `references/`、`scripts/` 与 `assets/` 共同提供路由、约束、生产资产和质量检查，请勿只复制单个文件。

<details>
<summary><strong>Claude Code</strong></summary>

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git ~/.claude/skills/academic-data-visualization
```

</details>

<details>
<summary><strong>Cursor</strong></summary>

保留完整 Skill，并按项目需要使用 [`install/cursor/.cursorrules`](install/cursor/.cursorrules)。

</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

使用 [`install/copilot/copilot-instructions.md`](install/copilot/copilot-instructions.md) 作为仓库级指令。

</details>

更新已有安装：

```bash
git -C ~/.codex/skills/academic-data-visualization pull
```

## 质量证据

当前仓库基线：

- **714 / 714** 条源分类归属完成可复现映射；
- **34 / 34** 类生产图型均有真实脚本、PNG 与 manifest；
- **88 / 88** 条触发边界用例判断正确；
- **26 / 26** 个 QA 用例命中预期，覆盖 **15 / 15** 类程序检查；
- 注册表 Schema、24 类生成文档、别名冲突、资产映射与 README 摘要均由 CI 审计。

```bash
python scripts/check_skill_metadata.py
python scripts/check_references.py
python scripts/check_chart_registry.py
python scripts/build_chart_registry.py --check
python scripts/generate_chart_catalog.py --check
python -m unittest discover -s tests -v
python scripts/trigger_benchmark.py
python scripts/qa_coverage.py
python -m compileall -q scripts assets/figures tests
```

只有 [`checklist.md`](references/checklist.md) 中的反模式、代码与导出、科学逻辑、最终渲染四轮检查全部完成，结果才可标记为 `READY`。

<details>
<summary><strong>仓库结构</strong></summary>

```text
academic-data-visualization/
├── SKILL.md                 # 精简决策入口与按需路由
├── AGENTS.md                # 架构规则、生成文件与必跑检查
├── agents/openai.yaml       # Codex 展示与默认提示元数据
├── references/              # 注册表、24 类目录、选图、期刊、配色、导出与 QA
├── scripts/                 # 生成、校验、组合、配色与灰度校样
├── tests/                   # taxonomy、路由与生成结果回归测试
├── assets/                  # 生产脚本、manifest、图鉴与配色预览
└── install/                 # Codex / Claude Code / Cursor / Copilot 适配文件
```

</details>

## 贡献与许可

新增图型时，请先登记 canonical record、别名、分类与真实实现状态，再运行目录生成器。只有同时提交真实脚本、PNG 和 `asset.yaml` 的图型才能标记为 `production_template`；不得为未实现图型伪造预览或资产路径。完整要求见 [`AGENTS.md`](AGENTS.md)。

本项目采用 [Apache-2.0](LICENSE) 许可证。
