"""Analyze module - トピック分析"""

import logging
import time
from typing import List, Dict

from src.config import (
    FEATURED_NEWS_FILE,
    GROUPED_NEWS_FILE,
    FINAL_REPORTS_FILE,
    ARTICLES_DIR,
    REQUEST_DELAY_SEC,
)
from src.utils.io import load_json, save_json
from src.utils.api import call_llm

logger = logging.getLogger(__name__)

ANALYSIS_PROMPT = """
あなたは伝説の蓄電池・電力業界アナリストです。
記事内容から業界人が唸る鋭い分析を日本語で行う。

【出力形式】
{
  "summary_points": ["核心1", "核心2", "核心3"],
  "insight": "業界解説150文字"
}
"""


def get_md_content(article_id: int) -> str:
    """Markdownファイルを取得"""
    try:
        with open(f"{ARTICLES_DIR}/{article_id}.md", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""


def analyze_topic(topic_name: str, combined_content: str, is_grouped: bool) -> Dict:
    """単一トピックをAI分析"""
    if is_grouped:
        user_input = f"トピック: {topic_name}\n\n複数ソース統合:\n{combined_content[:20000]}"
    else:
        user_input = f"トピック: {topic_name}\n\n記事本文:\n{combined_content[:15000]}"

    result = call_llm(ANALYSIS_PROMPT, user_input, {"type": "json_object"})

    if result:
        return result

    return {"summary_points": ["分析エラー"], "insight": "リトライ上限到達"}


def run_analyze() -> List[Dict]:
    """分析パイプライン実行"""
    articles = load_json(FEATURED_NEWS_FILE)
    groups = load_json(GROUPED_NEWS_FILE)

    if not articles or not groups:
        logger.error("featured_news.json または grouped_news.json が見つかりません")
        return []

    logger.info(f"{len(groups)} 個のトピックを分析中...")

    final_reports = []

    for i, group in enumerate(groups):
        topic_name = group.get("topic_name", "")
        aids = group.get("article_ids", [])
        is_grouped = group.get("is_grouped", False)

        logger.info(f"[{i + 1}/{len(groups)}] {topic_name}")

        # 本文収集
        combined = ""
        for aid in aids:
            content = get_md_content(aid)
            if is_grouped:
                combined += f"--- ソース(ID:{aid}) ---\n{content}\n\n"
            else:
                combined = content

        # 分析実行
        analysis = analyze_topic(topic_name, combined, is_grouped)

        # レポート作成
        report = {
            "topic_name": topic_name,
            "article_ids": aids,
            "articles": [a for a in articles if a.get("id") in aids],
            "is_grouped": is_grouped,
            "analysis": analysis,
        }
        final_reports.append(report)

        # 逐次保存
        save_json(final_reports, FINAL_REPORTS_FILE)

        logger.info("分析完了")
        time.sleep(REQUEST_DELAY_SEC)

    logger.info(f"{len(final_reports)} 件のレポートを生成")
    return final_reports


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_analyze()
