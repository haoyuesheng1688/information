# Cloud Automation

本项目现在支持 GitHub Actions 云端定时运行。即使本机电脑关机，GitHub 云端仍会在每天 08:30 中国时间触发。

## 云端执行路径

1. GitHub Actions 在 `00:30 UTC` 触发。
2. `scripts/daily_report.py` 调用 OpenAI Responses API 的 `web_search` 工具检索最新行业信息。
3. 生成 Markdown 报告并保存到 `reports/`。
4. 使用 Notion API 在 `infomation` 页面下创建日报子页面。
5. 将 `reports/` 和 `docs/last-run.json` 提交回 GitHub。

## 必需 GitHub Secrets

在 `haoyuesheng1688/information` 仓库中配置:

- `OPENAI_API_KEY`: 用于生成带联网检索的行业报告。
- `NOTION_TOKEN`: Notion internal integration secret。
- `NOTION_PARENT_PAGE_ID`: 可选；默认使用当前已验证的 `infomation` 页面 ID `36bc8717-dee0-812d-82d3-e2892298cd2c`。

## Notion 权限要求

Notion integration 必须被邀请到 `infomation` 页面，且拥有创建子页面和写入内容的权限。

## 手动触发验证

配置 Secrets 后，可在 GitHub 仓库的 Actions 页面运行:

`Daily low-temperature spray dryer intelligence` -> `Run workflow`

成功后应看到:

- 新的 `reports/YYYY-MM-DD-low-temperature-spray-dryer-market-report.md`
- Notion `infomation` 页面下的新日报
- `docs/last-run.json` 中的 Notion 页面 URL
