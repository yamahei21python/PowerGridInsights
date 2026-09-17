"""設定・定数定義 - Power Grid Insights"""

import os
from dotenv import load_dotenv

load_dotenv()

# API設定
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_FLASH = os.getenv("GEMINI_MODEL_FLASH", "gemini-3.1-flash-lite-preview")
GEMINI_MODEL_PRO = os.getenv("GEMINI_MODEL_PRO", "gemini-2.0-pro")
GEMINI_MODEL = GEMINI_MODEL_FLASH  # 後方互換性のため
MODEL_NAME = f"gemini/{GEMINI_MODEL_FLASH}"

# ファイルパス
NEWS_DATA_FILE = "news_data.json"
ONLY_TITLE_FILE = "only_title.json"
FEATURED_NEWS_FILE = "featured_news.json"
GROUPED_NEWS_FILE = "grouped_news.json"
ARTICLES_DIR = "articles_md"
FINAL_REPORTS_FILE = "final_reports.json"
ARCHIVE_DIR = "archive"
DATES_FILE = "dates.json"

# 処理パラメータ
MAX_ARTICLES = 1000
SIMILARITY_THRESHOLD = 0.7
API_RETRY_COUNT = 3
API_RETRY_DELAY_BASE = 30
REQUEST_DELAY_SEC = 5

# ニュースソース設定
NEWS_SOURCES = {
    "domestic": [
        {"name": "蓄電所ネット", "url": "https://bess-net.jp/", "type": "news"},
        {"name": "BESS NEWS", "url": "https://bessnews.jp/", "type": "news"},
        {"name": "AI電気速報", "url": "https://ai-denki-sokuho.com/", "type": "news"},
        {"name": "スマートグリッドフォーラム", "url": "https://sgforum.impress.co.jp/", "type": "news"},
        {"name": "日経BP メガソーラービジネス", "url": "https://xtech.nikkei.com/", "type": "news"},
        {"name": "SOLAR JOURNAL", "url": "https://solarjournal.jp/", "type": "news"},
        {"name": "新エネルギー新聞", "url": "https://www.shin-energy.com/", "type": "news"},
        {"name": "PV Magazine Japan", "url": "https://pvjapan.jp/", "type": "news"},
        {"name": "エネルギーフォーラム", "url": "https://energy-forum.co.jp/", "type": "news"},
        {"name": "電気新聞", "url": "https://www.denkishimbun.com/", "type": "news"},
        {"name": "環境ビジネスオンライン", "url": "https://www.kankyo-business.jp/", "type": "news"},
        {"name": "PR TIMES", "url": "https://prtimes.jp/", "type": "pr"},
        {"name": "時事通信", "url": "https://www.jiji.com/", "type": "news"},
    ],
    "regulation": [
        {"name": "経済産業省", "url": "https://www.meti.go.jp/", "type": "government"},
        {"name": "OCCTO", "url": "https://www.occto.or.jp/", "type": "government"},
        {"name": "資源エネルギー庁", "url": "https://www.enecho.meti.go.jp/", "type": "government"},
    ],
    "overseas": [
        {"name": "Energy Storage News", "url": "https://www.energy-storage.news/", "type": "news"},
        {"name": "PV Magazine", "url": "https://www.pv-magazine.com/", "type": "news"},
        {"name": "Utility Dive", "url": "https://www.utilitydive.com/", "type": "news"},
    ],
    "self": [
        {"name": "Daigas Energy", "url": "https://www.daigas-energy.co.jp/", "type": "company"},
    ],
}

# 検索キーワード
SEARCH_KEYWORDS = [
    "蓄電池",
    "系統用蓄電池",
    "BESS",
    "需給調整市場",
    "容量市場",
    "VPP",
    "DR",
    "EV充電",
    "再エネ",
    "PPA",
    "補助金",
    "制度改正",
    "アグリゲーター",
    "電力市場",
]

# ロギング
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
