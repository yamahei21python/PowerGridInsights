"""RSS フィード取得 - Power Grid Insights"""

import feedparser
import hashlib
import logging
from typing import List, Dict

from src.config import MAX_ARTICLES, NEWS_DATA_FILE
from src.utils.io import load_json, save_json

logger = logging.getLogger(__name__)


def generate_id(url: str) -> int:
    """URLから数値IDを生成"""
    return int(hashlib.md5(url.encode()).hexdigest(), 16) % 1000000


def fetch_from_rss(rss_url: str, source_name: str = "不明") -> List[Dict]:
    """RSSフィードから記事を取得"""
    logger.info(f"RSS取得中: {source_name} ({rss_url})")
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries[:50]:  # 最大50件
        articles.append({
            "id": generate_id(entry.link),
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")[:500],
            "site_name": source_name,
            "source_type": "rss",
        })

    logger.info(f"{len(articles)} 件の記事を取得 ({source_name})")
    return articles


def fetch_from_google_rss(keyword: str = "蓄電池") -> List[Dict]:
    """GoogleニュースRSSから記事を取得"""
    rss_url = f"https://news.google.com/rss/search?q={keyword}+when:1d&hl=ja&gl=JP&ceid=JP:ja"
    return fetch_from_rss(rss_url, "Googleニュース")


def merge_articles(new_articles: List[Dict], filename: str = NEWS_DATA_FILE) -> int:
    """既存データとマージ（重複排除）"""
    existing_data = load_json(filename)
    existing_articles = existing_data.get("articles", []) if existing_data else []

    existing_links = {a["link"] for a in existing_articles}
    merged = existing_articles.copy()
    new_count = 0

    for article in new_articles:
        if article["link"] not in existing_links:
            merged.append(article)
            existing_links.add(article["link"])
            new_count += 1

    # 最新1000件のみ保持
    if len(merged) > MAX_ARTICLES:
        merged = merged[-MAX_ARTICLES:]

    from datetime import datetime
    save_json(
        {
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_count": len(merged),
            "articles": merged,
        },
        filename,
    )

    logger.info(f"{new_count} 件追加。合計: {len(merged)}")
    return new_count
