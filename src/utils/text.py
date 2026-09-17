"""テキスト処理ユーティリティ - Power Grid Insights"""

import re
from typing import List


def truncate_text(text: str, max_length: int = 500) -> str:
    """テキストを切り詰める"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def extract_keywords(text: str, keywords: List[str]) -> List[str]:
    """テキストからキーワードを抽出"""
    found = []
    text_lower = text.lower()
    for keyword in keywords:
        if keyword.lower() in text_lower:
            found.append(keyword)
    return found


def clean_html(html: str) -> str:
    """HTMLタグを除去"""
    clean = re.sub(r'<[^>]+>', '', html)
    return clean.strip()


def normalize_url(url: str) -> str:
    """URLを正規化"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url.rstrip('/')
