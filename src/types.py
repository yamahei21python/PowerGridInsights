"""型定義 - Power Grid Insights"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class NewsArticle:
    """ニュース記事"""
    id: int
    title: str
    link: str
    published: str
    summary: str
    site_name: str
    source_type: str = "news"  # news, pr, government, company
    fetched_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


@dataclass
class TopicGroup:
    """トピックグループ"""
    topic_name: str
    article_ids: list[int]
    is_grouped: bool = False


@dataclass
class AnalysisReport:
    """分析レポート"""
    topic_name: str
    article_ids: list[int]
    articles: list[dict]
    is_grouped: bool
    analysis: dict  # {"summary_points": [...], "insight": "..."}


@dataclass
class ProcessedArticle:
    """AI処理済み記事"""
    id: int
    title: str
    link: str
    published: str
    site_name: str
    source_type: str
    score: float  # 0.0-1.0
    is_featured: bool
    summary: str = ""
    keywords: list[str] = field(default_factory=list)
