# 图型覆盖审计

## 审计结论

用户补充的源文件包含 24 个一级类别、714 条编号分类条目。本版本已经逐条解析并映射：

- 源类别：24 / 24；
- 源分类归属：714 / 714；
- 未映射源条目：0；
- canonical chart records：665；
- 源清单图型：625；
- 仓库扩展图型：40；
- `production_template`：34；
- `reusable_pattern`：228；
- `on_demand`：403。

`source_expectation.source_complete` 已更新为 `true`。注册表、源清单和 24 个分类文档之间的对应关系由测试与 CI 强制验证。

## 源清单处理

`references/chart-taxonomy-source.md` 保存 714 条原始名称及其 canonical ID。导入遵循以下规则：

1. 原始条目和跨类别重复均保留为 source membership；
2. 同一图型只保存一个 canonical record；
3. 中英文名、缩写和常见变体进入别名索引；
4. 同名异义必须显式声明，不使用模糊猜测；
5. 未出现在源清单、但属于原仓库能力的记录标记为 `repository_extension`。

当前明确消歧的术语包括：

- “漏斗图”：元分析发表偏倚与流程转化；
- “棒棒糖图”：通用排序与突变位点；
- “瀑布图”：一般增减贡献与肿瘤疗效；
- “蜘蛛图”：多指标雷达图与肿瘤负荷纵向图。

## 类别对齐

24 类名称和顺序已经与补充源文件对齐。相较 2.0 版，新增或重新独立表达了：

- 实验设计与组间差异；
- 质性研究与文本分析；
- 层级与分类结构；
- 三维、曲面与科学计算；
- 工程质量与过程控制；
- 因果机制与理论模型；
- 研究流程与论文规范。

原有图型通过 category remap 保留，不因类别重排丢失能力。

## 生产资产真实性

`assets/figures/` 下 34 个真实生产目录保持不变。每个生产模板仍必须同时具有：

- 真实 Python / R 脚本；
- PNG 预览；
- `asset.yaml`；
- registry 与 manifest 双向映射；
- 可执行 QA 命令。

新增源图型没有被批量伪装为生产资产。只有统计与视觉规则可直接复用的条目标为 `reusable_pattern`；地图、专业流程、文本网络、三维场和领域模型等依赖数据契约的图型保持 `on_demand`。

## 自动检查

以下检查共同保证 714 条覆盖不回退：

- `scripts/import_source_taxonomy.py`：要求源文件正好包含 24 类和 714 条编号记录；
- `scripts/check_chart_registry.py`：按分类、canonical ID 和原始标签逐条核对；
- `scripts/generate_chart_catalog.py --check`：检查 24 个分类文档、别名索引、README 和机器目录；
- `tests/test_chart_registry.py`：断言 714 / 714、来源状态和生产资产真实性；
- `tests/test_chart_routing.py`：检查中英文名称、缩写和同名异义；
- GitHub Actions：在 Windows 与 Ubuntu 上运行全部确定性检查。

## 兼容性

- 保留旧 6 组 × 16 个图鉴和公开路径；
- 保留 34 个生产资产目录及 canonical ID；
- `directory-map.md` 仍只列真实生产资产；
- `SKILL.md` 仍是精简路由入口，详细图型知识按需读取；
- 未 force push，也未覆盖用户历史。
