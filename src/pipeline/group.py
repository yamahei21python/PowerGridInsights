"""Group module - トピック名寄せ"""

import logging
from typing import List, Dict

from src.config import FEATURED_NEWS_FILE, GROUPED_NEWS_FILE
from src.utils.io import load_json, save_json
from src.utils.api import call_llm

logger = logging.getLogger(__name__)

GROUPING_PROMPT = """
あなたは蓄電池・電力業界のニュース編集者です。
以下の記事タイトルをグループ化してください。

【グループ化ルール】
- 同一トピックの記事をグループ化
- 1グループあたり2-5件
- グループ名は簡潔に（20文字以内）

【出力形式】
{
  "groups": [
    {
      "topic_name": "グループ名",
      "article_ids": [1, 2, 3],
      "is_grouped": true
    }
  ]
}
"""


def run_group() -> List[Dict]:
    """トピック名寄せパイプライン実行"""
    articles_data = load_json(FEATURED_NEWS_FILE)
    if not articles_data or "articles" not in articles_data:
        logger.error("featured_news.json が見つかりません")
        return []

    articles = articles_data["articles"]
    logger.info(f"{len(articles)} 件の記事をグループ化中...")

    # 記事タイトルを整理
    article_list = [{"id": a["id"], "title": a["title"]} for a in articles]

    user_input = "記事一覧:\n"
    for a in article_list:
        user_input += f"- ID:{a['id']} {a['title']}\n"

    result = call_llm(GROUPING_PROMPT, user_input, {"type": "json_object"})

    if result and "groups" in result:
        groups = result["groups"]
    else:
        # フォールバック: 記事を単一グループに
        groups = [{
            "topic_name": "蓄電池・電力ニュース",
            "article_ids": [a["id"] for a in articles],
            "is_grouped": False,
        }]

    save_json(groups, GROUPED_NEWS_FILE)
    logger.info(f"{len(groups)} 個のグループを生成")
    return groups


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_group()
