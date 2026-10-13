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