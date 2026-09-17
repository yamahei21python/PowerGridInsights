"""Fetch main - ニュース収集メイン"""

import logging
from typing import List, Dict

from src.config import SEARCH_KEYWORDS
from src.fetch.rss import fetch_from_google_rss, merge_articles

logger = logging.getLogger(__name__)


def run_fetch() -> List[Dict]:
    """ニュース収集パイプライン実行"""
    all_articles = []

    # Googleニュースから収集（主要キーワード）
    for keyword in SEARCH_KEYWORDS[:5]:  # 上位5キーワードで収集
        articles = fetch_from_google_rss(keyword)
        all_articles.extend(articles)

    # 重複排除してマージ
    new_count = merge_articles(all_articles)

    logger.info(f"収集完了: {new_count} 件の新規記事")
    return all_articles


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_fetch()
