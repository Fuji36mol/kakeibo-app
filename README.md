# kakeibo-app
# 家計簿アプリ

収入・支出を記録し、集計やグラフで確認できるコマンドラインツールです。

## 使い方
pip install -r requirements.txt
python main.py

## データの形
1件の記録は次の項目を持つ辞書です。
- date：日付（文字列、例："2026-10-13"）
- amount：金額（整数。収入はプラス、支出はマイナス）
- category：カテゴリ（文字列、例："食費"）
- memo：メモ（文字列、空でもよい）

## storage.py の関数
- load_records(path="data.json") → 記録のリストを返す。ファイルがなければ空のリスト
- save_records(records, path="data.json") → 記録のリストを保存する

## ファイル構成
| ファイル | 内容 | 担当 |
|---|---|---|
| storage.py | データの読み書き | Fuji |
| main.py | メニュー | 全員 |
| records.py | 入力・一覧表示・削除 | 岩月 |
| summary.py | 合計・残高、カテゴリ別集計、月の切り替え | Fuji |
| report.py | グラフ表示、予算の警告 | 岩月 |