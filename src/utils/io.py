"""I/O ユーティリティ - Power Grid Insights"""

import json
import logging
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


def load_json(filename: str) -> Optional[Any]:
    """JSONファイルを読み込む"""
    try:
        filepath = Path(filename)
        if not filepath.exists():
            return None
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"JSON読み込みエラー ({filename}): {e}")
        return None


def save_json(data: Any, filename: str) -> bool:
    """JSONファイルに保存"""
    try:
        filepath = Path(filename)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logger.error(f"JSON保存エラー ({filename}): {e}")
        return False


def read_text_file(filename: str) -> Optional[str]:
    """テキストファイルを読み込む"""
    try:
        filepath = Path(filename)
        if not filepath.exists():
            return None
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"テキスト読み込みエラー ({filename}): {e}")
        return None


def ensure_dir(directory: str) -> None:
    """ディレクトリが存在することを確認"""
    Path(directory).mkdir(parents=True, exist_ok=True)
