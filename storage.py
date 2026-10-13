"""家計簿データの読み書きを担当するモジュール"""
import json
import os

DATA_FILE = "data.json"


def load_records(path=DATA_FILE):
    """記録のリストを読み込んで返す。ファイルがなければ空のリストを返す。"""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_records(records, path=DATA_FILE):
    """記録のリストをファイルに保存する。"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)