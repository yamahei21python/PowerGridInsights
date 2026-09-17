"""Archive module - アーカイブ処理"""

import logging
import shutil
from datetime import datetime
from pathlib import Path

from src.config import (
    FINAL_REPORTS_FILE,
    ARCHIVE_DIR,
    DATES_FILE,
)
from src.utils.io import load_json, save_json

logger = logging.getLogger(__name__)


def run_archive() -> str:
    """アーカイブパイプライン実行"""
    reports = load_json(FINAL_REPORTS_FILE)
    if not reports:
        logger.error("final_reports.json が見つかりません")
        return ""

    # 日付を取得
    today = datetime.now().strftime("%Y-%m-%d")
    archive_dir = Path(ARCHIVE_DIR) / today
    archive_dir.mkdir(parents=True, exist_ok=True)

    # レポートをアーカイブ
    archive_file = archive_dir / "reports.json"
    save_json(reports, str(archive_file))

    # 日付インデックスを更新
    dates = load_json(DATES_FILE) or []
    if today not in dates:
        dates.insert(0, today)
        dates = dates[:365]  # 最大365日分
        save_json(dates, DATES_FILE)

    logger.info(f"アーカイブ完了: {archive_dir}")
    return today


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_archive()
