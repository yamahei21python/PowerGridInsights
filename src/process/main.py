"""Process main - AI分析メイン"""

import logging
from typing import List, Dict

from src.config import (
    NEWS_DATA_FILE,
    FEATURED_NEWS_FILE,
    SIMILARITY_THRESHOLD,
)
from src.utils.io import load_json, save_json
from src.utils.api import call_llm

logger = logging.getLogger(__name__)

# AI分析プロンプト
SCORING_PROMPT = """
あなたは蓄電池・電力業界のアナリストです。
以下のニュース記事を評価し、重要度スコア（0.0-1.0）を付与してください。

【評価基準】
- 蓄電池・系統用蓄電池（BESS）に関連: +0.3
- 需給調整市場・容量市場に関連: +0.3
- VPP・DR・EV充電に関連: +0.2
- 補助金・制度改正に関連: +0.2
- Daigas Energyに関連: +0.2

【出力形式】
{
  "score": 0.8,
  "is_featured": true,
  "keywords": ["蓄電池", "系統用蓄電池", "需給調整市場"]
}
"""


def score_article(article: Dict) -> Dict:
    """単一記事をAI評価"""
    user_input = f"""
タイトル: {article['title']}
本文: {article.get('summary', '')[:1000]}
配信元: {article['site_name']}
"""

    result = call_llm(SCORING_PROMPT, user_input, {"type": "json_object"})

    if result:
        article["score"] = result.get("score", 0.0)
        article["is_featured"] = result.get("is_featured", False)
        article["keywords"] = result.get("keywords", [])
    else:
        article["score"] = 0.0
        article["is_featured"] = False
        article["keywords"] = []

    return article


def run_process() -> List[Dict]:
    """AI分析パイプライン実行"""
    data = load_json(NEWS_DATA_FILE)
    if not data or "articles" not in data:
        logger.error("news_data.json が見つかりません")
        return []

    articles = data["articles"]
    logger.info(f"{len(articles)} 件の記事を分析中...")

    featured = []
    for i, article in enumerate(articles):
        logger.info(f"[{i + 1}/{len(articles)}] {article['title'][:50]}...")

        scored = score_article(article)
        if scored.get("is_featured") and scored.get("score", 0) >= 0.5:
            featured.append(scored)

    # 重要記事を保存
    save_json(
        {
            "updated_at": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_count": len(featured),
            "articles": featured,
        },
        FEATURED_NEWS_FILE,
    )

    logger.info(f"分析完了: {len(featured)} 件の重要記事を抽出")
    return featured


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_process()
