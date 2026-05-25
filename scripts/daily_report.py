import datetime as dt
import json
import os
import pathlib
import re
import sys
from typing import Any

import requests


ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
DOCS_DIR = ROOT / "docs"
KEYWORDS_PATH = ROOT / "config" / "keywords.json"
DEFAULT_NOTION_PARENT_PAGE_ID = "36bc8717-dee0-812d-82d3-e2892298cd2c"


def require_env(name: str) -> str:
    value = os.environ.get(name, "").replace("\ufeff", "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def load_keywords() -> dict[str, Any]:
    return json.loads(KEYWORDS_PATH.read_text(encoding="utf-8"))


def today_cn() -> dt.date:
    # GitHub hosted runners are UTC. China is UTC+8 and has no DST.
    return (dt.datetime.utcnow() + dt.timedelta(hours=8)).date()


def extract_response_text(payload: dict[str, Any]) -> str:
    if isinstance(payload.get("output_text"), str) and payload["output_text"].strip():
        return payload["output_text"].strip()

    parts: list[str] = []
    for item in payload.get("output", []):
        for content in item.get("content", []):
            text = content.get("text")
            if isinstance(text, str):
                parts.append(text)
    text = "\n".join(parts).strip()
    if not text:
        raise RuntimeError("OpenAI response did not contain report text.")
    return text


def generate_report(report_date: dt.date, keywords: dict[str, Any]) -> str:
    api_key = require_env("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL", "gpt-5").strip() or "gpt-5"

    prompt = f"""
你是工业自动化与生物医药装备领域的深度市场分析与研发顾问。

任务日期: {report_date.isoformat()}
项目关键词配置:
{json.dumps(keywords, ensure_ascii=False, indent=2)}

请联网检索当天或最近 24-72 小时内与低温喷雾干燥、35C 进风、冻干替代、GLP-1/多肽、biologics/proteins/peptides、pharmaceutical spray drying CDMO、peptide CDMO、益生菌、酶制剂、功能食品、天然提取物、新材料相关的全球动态。

输出一份严格 Markdown 报告，标题必须为:
# {report_date.isoformat()} 低温喷雾干燥机行业情报日报

必须包含以下章节:
1. 执行摘要
2. 全球市场动态 (Global Market Dynamics)
3. 研发工艺匹配报告 (R&D & Process Alignment Report)
4. 市场与前景评估报告 (Market & Outlook Report)
5. 每日精准潜在客户画像 (Potential Customers & Leads)
6. 当日行动建议
7. 来源链接

强制标注规则:
- 🔴 **红色标注 / 关键技术/工艺突破/核心痛点**
- 🔵 **蓝色标注 / 全球市场动态/政策趋势**
- 🟢 **绿色标注 / 潜在客户/商机/批量化产线需求**

工程约束:
- 不得泛化宣传 35C 低温喷雾干燥适用于所有物料。
- 对 GLP-1、多肽、蛋白、酶制剂、益生菌必须提出可验证的小试指标。
- 区分已验证事实、来源推断、我方可切入机会。
- 来源链接必须列出可点击 URL。
"""

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "tools": [{"type": "web_search"}],
            "tool_choice": "auto",
            "input": prompt,
        },
        timeout=600,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"OpenAI API error {response.status_code}: {response.text}")
    return extract_response_text(response.json())


def save_report(report_date: dt.date, report: str) -> pathlib.Path:
    REPORTS_DIR.mkdir(exist_ok=True)
    path = REPORTS_DIR / f"{report_date.isoformat()}-low-temperature-spray-dryer-market-report.md"
    path.write_text(report.rstrip() + "\n", encoding="utf-8")
    return path


def notion_headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {require_env('NOTION_TOKEN')}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }


def rich_text(text: str) -> list[dict[str, Any]]:
    # Notion rich_text text content limit is 2000 chars.
    chunks = [text[i : i + 1900] for i in range(0, len(text), 1900)] or [""]
    return [{"type": "text", "text": {"content": chunk}} for chunk in chunks]


def block_from_line(line: str, numbered_state: dict[str, int]) -> dict[str, Any] | None:
    stripped = line.strip()
    if not stripped:
        return None
    if stripped.startswith("# "):
        return {"object": "block", "type": "heading_1", "heading_1": {"rich_text": rich_text(stripped[2:])}}
    if stripped.startswith("## "):
        return {"object": "block", "type": "heading_2", "heading_2": {"rich_text": rich_text(stripped[3:])}}
    if stripped.startswith("### "):
        return {"object": "block", "type": "heading_3", "heading_3": {"rich_text": rich_text(stripped[4:])}}
    if stripped.startswith("- "):
        return {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": rich_text(stripped[2:])}}
    if re.match(r"^\d+\.\s+", stripped):
        return {
            "object": "block",
            "type": "numbered_list_item",
            "numbered_list_item": {"rich_text": rich_text(re.sub(r"^\d+\.\s+", "", stripped))},
        }
    if stripped.startswith("|"):
        return {"object": "block", "type": "code", "code": {"rich_text": rich_text(stripped), "language": "plain text"}}
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rich_text(stripped)}}


def markdown_to_blocks(markdown: str) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    numbered_state = {"n": 0}
    for line in markdown.splitlines():
        block = block_from_line(line, numbered_state)
        if block:
            blocks.append(block)
    return blocks


def create_notion_page(report_date: dt.date, report: str) -> dict[str, Any]:
    parent_page_id = os.environ.get("NOTION_PARENT_PAGE_ID", "").strip() or DEFAULT_NOTION_PARENT_PAGE_ID
    title = f"{report_date.isoformat()} 低温喷雾干燥机行业情报日报"

    create_response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=notion_headers(),
        json={
            "parent": {"type": "page_id", "page_id": parent_page_id},
            "properties": {"title": {"title": [{"type": "text", "text": {"content": title}}]}},
        },
        timeout=60,
    )
    if create_response.status_code >= 400:
        raise RuntimeError(f"Notion create page error {create_response.status_code}: {create_response.text}")

    page = create_response.json()
    page_id = page["id"]
    blocks = markdown_to_blocks(report)
    for start in range(0, len(blocks), 90):
        chunk = blocks[start : start + 90]
        append_response = requests.patch(
            f"https://api.notion.com/v1/blocks/{page_id}/children",
            headers=notion_headers(),
            json={"children": chunk},
            timeout=60,
        )
        if append_response.status_code >= 400:
            raise RuntimeError(f"Notion append blocks error {append_response.status_code}: {append_response.text}")

    verify_response = requests.get(f"https://api.notion.com/v1/pages/{page_id}", headers=notion_headers(), timeout=60)
    if verify_response.status_code >= 400:
        raise RuntimeError(f"Notion verify page error {verify_response.status_code}: {verify_response.text}")
    verified = verify_response.json()
    actual_parent = verified.get("parent", {}).get("page_id", "").replace("-", "")
    expected_parent = parent_page_id.replace("-", "")
    if actual_parent != expected_parent:
        raise RuntimeError(f"Notion parent verification failed: expected {parent_page_id}, got {verified.get('parent')}")

    return {"id": page_id, "url": page.get("url"), "parent_page_id": parent_page_id, "title": title}


def write_last_run(report_path: pathlib.Path, notion_page: dict[str, Any]) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    payload = {
        "ran_at_utc": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "report_path": str(report_path.as_posix()),
        "notion_page": notion_page,
    }
    (DOCS_DIR / "last-run.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    report_date = today_cn()
    keywords = load_keywords()
    report = generate_report(report_date, keywords)
    report_path = save_report(report_date, report)
    notion_page = create_notion_page(report_date, report)
    write_last_run(report_path, notion_page)
    print(json.dumps({"report": str(report_path), "notion": notion_page}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"daily_report failed: {exc}", file=sys.stderr)
        raise
