"""グラフ表示と予算の警告を担当するファイル（フェーズ4）
単独で動作確認するときは python report.py で実行できる。"""

from datetime import date

import storage

# 1か月の支出の予算（円）
BUDGET = 30000

# 棒グラフの一番長い棒の長さ
BAR_MAX = 20


def show_graph():
    """支出をカテゴリ別に集計して、文字の棒グラフで表示する。"""
    records = storage.load_records()

    # カテゴリごとに支出を足していく
    totals = {}
    for r in records:
        if r["type"] == "支出":
            totals[r["category"]] = totals.get(r["category"], 0) + r["amount"]

    print("\n--- カテゴリ別の支出グラフ ---")
    if len(totals) == 0:
        print("支出の記録がありません")
        return

    biggest = max(totals.values())
    # 金額の大きい順に並べて表示
    for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        length = max(1, round(amount / biggest * BAR_MAX))
        print(f"{category:<6} {'■' * length} {amount:,}円")


def check_budget():
    """今月の支出の合計を予算と比べて、警告を出す。"""
    records = storage.load_records()
    this_month = date.today().strftime("%Y-%m")  # 例：2026-10

    spent = 0
    for r in records:
        if r["type"] == "支出" and r["date"].startswith(this_month):
            spent += r["amount"]

    print(f"\n--- 今月（{this_month}）の予算 ---")
    print(f"予算：{BUDGET:,}円　支出：{spent:,}円　残り：{BUDGET - spent:,}円")

    if spent > BUDGET:
        print(f"【注意】予算を{spent - BUDGET:,}円オーバーしています！")
    elif spent >= BUDGET * 0.8:
        print("【注意】予算の8割を超えました。使いすぎに注意！")
    else:
        print("予算内です")


def show_report():
    """グラフと予算チェックをまとめて表示する（メニュー5から呼ぶ）。"""
    show_graph()
    check_budget()


if __name__ == "__main__":
    show_report()