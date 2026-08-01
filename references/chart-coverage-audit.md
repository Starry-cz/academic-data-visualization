# 图型覆盖与执行状态审计

## 结论

注册表覆盖与生产执行能力是两个不同问题。当前知识层保持 24 类完整路由；生产层只承认通过 Manifest v2 门禁的资产，不再用“有脚本 + 有 PNG”代替可运行、可复现与可交付证据。

## 当前状态

机器可读的实时统计见 `chart-registry-stats.json`。本次 v2 迁移后的基线为：

- 24 个研究问题分类；
- 678 个 canonical chart records；
- 12 个 `production_verified + release_passed` 模板；
- 29 个注册表内 `legacy_example`，以及为避免破坏公开路径而保留的历史 successor 示例；
- 235 个 `pattern`；
- 402 个 `none`。

源分类归属数量仍由注册表和 CI 审计，但不作为 README 的用户价值指标。

## 三轴状态模型

| 轴 | 状态 | 说明 |
|---|---|---|
| 知识 | `registered / reviewed / deprecated` | 图型定义和约束是否经过审阅 |
| 实现 | `none / pattern / legacy_example / demo_runnable / production_verified / deprecated` | 仓库中实际存在什么实现 |
| 验证 | `untested / syntax_parsed / rendered_passed / release_passed / failed` | 当前证据强度 |

任何一轴都不得从另一轴推断。预览不证明实现，语法通过不证明渲染，自动 QA 不证明视觉质量。

## 生产资产证据

每个已验证模板必须保存：

- 确定性 demo 与固定 CSV fixture；
- 同一统一入口的两次真实执行记录；
- PDF、SVG、RGB PNG、灰度图、源数据、元数据、替代文本；
- QA 报告、运行记录、fixture 与产物哈希；
- 最终尺寸视觉复核记录；
- 明确的字体、Python 与依赖版本。

## 自动检查

- `check_chart_registry.py`：Schema、三轴状态、分类、别名与资产路径；
- `build_chart_registry.py --check`：Manifest v2 与真实文件证据；
- `verify_production_assets.py`：demo 与输入 fixture 的真实执行和产物 QA；
- `generate_chart_catalog.py --check`：24 个分类文档和 README 用户摘要；
- `generate_directory_map.py --check`：生产模板与历史示例分区；
- `check_showcase_lock.py`：精选图和配色库不漂移；
- GitHub Actions：Windows/Linux 可执行验证与 R 源文件解析。

## 保留策略

原有 `assets/figures/` 路径和图鉴继续保留，但默认属于历史示例。新模板存放于 `templates/production-verified/<canonical-id>/`。升级状态只能通过真实证据完成，不能批量改字段或伪造预览。
