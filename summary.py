"""合計・残高、カテゴリ別集計、月の切り替えを担当するモジュール"""
from rich.console import Console
from rich.table import Table

console = Console()


def get_months(records):
    """記録に含まれる月（"YYYY-MM"）を新しい順のリストで返す"""
    months = {r["date"][:7] for r in records}
    return sorted(months, reverse=True)


def filter_by_month(records, month):
    """指定した月の記録だけを返す。month が None なら全件を返す"""
    if month is None:
        return records
    return [r for r in records if r["date"].startswith(month)]


def calc_totals(records):
    """(収入合計, 支出合計, 残高) を返す。支出合計は正の数で返す"""
    income = sum(r["amount"] for r in records if r["amount"] > 0)
    expense = -sum(r["amount"] for r in records if r["amount"] < 0)
    return income, expense, income - expense


def calc_by_category(records):
    """支出をカテゴリ別に合計し、金額の大きい順の辞書で返す"""
    totals = {}
    for r in records:
        if r["amount"] < 0:
            totals[r["category"]] = totals.get(r["category"], 0) - r["amount"]
    return dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))

def choose_month(records):
    """集計する月を選ばせる。全期間なら None を返す"""
    months = get_months(records)
    print("\n集計する期間を選んでください")
    print("0. 全期間")
    for i, m in enumerate(months, start=1):
        print(f"{i}. {m}")
    choice = input("番号：")
    if choice.isdigit() and 1 <= int(choice) <= len(months):
        return months[int(choice) - 1]
    return None


def show_summary(records):
    """選んだ期間の収支とカテゴリ別支出を表で表示する"""
    if not records:
        print("記録がありません")
        return

    month = choose_month(records)
    target = filter_by_month(records, month)
    label = month if month else "全期間"

    # 収支の表
    income, expense, balance = calc_totals(target)
    color = "red" if balance < 0 else "green"
    table = Table(title=f"{label} の収支")
    table.add_column("項目")
    table.add_column("金額", justify="right")
    table.add_row("収入", f"{income:,}円")
    table.add_row("支出", f"{expense:,}円")
    table.add_row("残高", f"[{color}]{balance:,}円[/]")
    console.print(table)

    # カテゴリ別支出の表
    by_cat = calc_by_category(target)
    if by_cat:
        cat_table = Table(title=f"{label} のカテゴリ別支出")
        cat_table.add_column("カテゴリ")
        cat_table.add_column("金額", justify="right")
        cat_table.add_column("割合", justify="right")
        for cat, amount in by_cat.items():
            cat_table.add_row(cat, f"{amount:,}円", f"{amount / expense:.0%}")
        console.print(cat_table)


if __name__ == "__main__":
    import storage
    show_summary(storage.load_records("sample_data.json"))