"""Process main - AI分析メイン"""

import json
import logging
from typing import List, Dict, Tuple

from src.config import (
    NEWS_DATA_FILE,
    ONLY_TITLE_FILE,
    FEATURED_NEWS_FILE,
    SIMILARITY_THRESHOLD,
)
from src.utils.io import load_json, save_json
from src.utils.api import call_llm
from src.utils.text import (
    get_similarity,
    normalize_title,
    get_site_priority,
    is_major_media,
)

logger = logging.getLogger(__name__)

# AI分析プロンプト
SCORING_PROMPT = """
あなたは熟練の業界アナリストです。
蓄電池・電力ニュースの重要度を1〜100点でスコアリングしてください。

【判定基準】
1. 地方紙・テレビ局は【1〜20点】。ただし地域固有の一次情報は【70〜90点】
2. 専門メディアは【50〜100点】
3. 高評価: 制度改正・市場動向・大型プロジェクト・技術革新
4. 低評価: 一般的なニュース・個人向け製品発表

【出力】JSON配列:
[
  {
    "id": [入力のid],
    "primary_category": "[カテゴリ名または'Noise']",
    "reason": "[判定理由 50文字以内]",
    "score": [1-100],
    "is_highly_important": boolean
  }
]
"""


def deduplicate_articles(
    articles: List[Dict], threshold: float = SIMILARITY_THRESHOLD
) -> List[Dict]:
    """類似記事を排除（圧縮）"""
    unique_map = {}

    for article in articles:
        if not is_major_media(article.get("site_name", "")):
            continue

        norm_title = normalize_title(article.get("title", ""))
        is_dup = False

        for key in list(unique_map.keys()):
            if get_similarity(norm_title, key) > threshold:
                if get_site_priority(article.get("site_name", "")) > get_site_priority(
                    unique_map[key].get("site_name", "")
                ):
                    del unique_map[key]
                    unique_map[norm_title] = article
                is_dup = True
                break

        if not is_dup:
            unique_map[norm_title] = article

    return list(unique_map.values())


def create_only_title_json() -> Tuple[List[Dict], List[Dict]]:
    """only_title.json作成（重複排除後）"""
    data = load_json(NEWS_DATA_FILE)
    if not data:
        logger.error("news_data.jsonが見つかりません")
        return [], []

    raw_articles = data.get("articles", [])
    logger.info(f"全記事数: {len(raw_articles)} 件")

    compressed = deduplicate_articles(raw_articles)
    removed = len(raw_articles) - len(compressed)
    logger.info(f"類似排除: {removed} 件。判定対象: {len(compressed)} 件")

    only_titles = [
        {"id": a.get("id"), "title": a.get("title"), "site_name": a.get("site_name")}
        for a in compressed
    ]

    save_json(only_titles, ONLY_TITLE_FILE)
    return only_titles, compressed


def process_news_with_ai(
    only_titles: List[Dict], original_articles: List[Dict]
) -> List[Dict]:
    """AIでニュースを判定・スコアリング"""
    featured = []
    results_map = {}

    user_prompt = json.dumps(only_titles, ensure_ascii=False, indent=2)
    result = call_llm(SCORING_PROMPT, user_prompt, {"type": "json_object"})

    if result:
        if isinstance(result, list):
            for r in result:
                results_map[r["id"]] = r
        elif isinstance(result, dict) and "groups" in result:
            for r in result.get("groups", []):
                results_map[r["id"]] = r

    for article in original_articles:
        aid = article.get("id")
        if aid in results_map:
            article.update(results_map[aid])
            if article.get("is_highly_important") or article.get("score", 0) >= 70:
                featured.append(article)
        elif str(aid) in results_map:
            article.update(results_map[str(aid)])
            if article.get("is_highly_important") or article.get("score", 0) >= 70:
                featured.append(article)

    save_json(featured, FEATURED_NEWS_FILE)
    logger.info(f"重要記事: {len(featured)} 件を抽出")
    return featured


def run_process() -> List[Dict]:
    """プロセスパイプライン実行"""
    only_titles, compressed = create_only_title_json()
    if only_titles:
        return process_news_with_ai(only_titles, compressed)
    return []


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_process()
