# Low-Temperature Spray Dryer Intelligence

本仓库是 `D:\skills\codex\information` 的项目隔离工作区，用于生成和归档低温喷雾干燥机行业情报。

## 固定目标

- 核心设备: 35C 进风低温喷雾干燥机
- 目标价值: 替代冻干、保留活性、连续化生产、实验室到市场放大、节能
- Notion 页面: `infomation`
- GitHub 仓库: `haoyuesheng1688/information`
- 自动化时间: 每天 08:30

## 文件结构

- `AGENTS.md`: 项目级执行规则和报告格式。
- `config/keywords.json`: 关键词、行业优先级、颜色标注规则。
- `reports/`: 每日 Markdown 报告归档。
- `docs/`: 运行说明和验证记录。

## 验收标准

1. 每日报告必须包含来源链接。
2. 每日报告必须保存到 `reports/`。
3. 每日报告必须写入 Notion `infomation` 页面下。
4. 每日报告必须同步到 GitHub。
5. 所有自动化只在本项目目录内运行，避免跨项目污染。
