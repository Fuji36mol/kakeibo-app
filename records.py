"""記録の入力・一覧表示・削除を担当するファイル（フェーズ2）"""

from datetime import date

import storage


def add_record():
    """記録を1件入力して保存する。"""
    print("\n--- 記録の入力 ---")

    # 日付（何も入力しなければ今日）
    day = input(f"日付（例：{date.today()}、空欄で今日）：").strip()
    if day == "":
        day = str(date.today())

    # 収入か支出か
    kind = input("1:収入  2:支出 を選んでください：").strip()
    if kind == "1":
        kind = "収入"
    elif kind == "2":
        kind = "支出"
    else:
        print("1か2を入力してください。入力をやめます。")
        return

    category = input("カテゴリ（例：食費、交通費、バイト）：").strip()

    # 金額（正の整数だけ受け付ける）
    amount = input("金額（円）：").strip()
    if not amount.isdigit() or int(amount) == 0:
        print("金額は1以上の数字で入力してください。入力をやめます。")
        return

    memo = input("メモ（空欄でもOK）：").strip()

    # 全部読む → 1件足す → 全部書き直す
    records = storage.load_records()
    records.append({
        "date": day,
        "type": kind,
        "category": category,
        "amount": int(amount),
        "memo": memo,
    })
    storage.save_records(records)
    print("記録しました！")


def show_records():
    """記録を番号付きで全部表示する。"""
    records = storage.load_records()
    print("\n--- 記録の一覧 ---")
    if len(records) == 0:
        print("まだ記録がありません")
        return

    for number, r in enumerate(records, start=1):
        print(f"{number}. {r['date']}  {r['type']}  {r['category']}  "
              f"{r['amount']:,}円  {r['memo']}")


def delete_record():
    """一覧から番号を選んで1件削除する。"""
    records = storage.load_records()
    if len(records) == 0:
        print("\n削除できる記録がありません")
        return

    show_records()
    number = input("削除する番号（やめるときは空欄）：").strip()
    if number == "":
        print("削除をやめました")
        return
    if not number.isdigit() or not (1 <= int(number) <= len(records)):
        print(f"1〜{len(records)}の番号を入力してください")
        return

    # 全部読む → 1件消す → 全部書き直す
    removed = records.pop(int(number) - 1)
    storage.save_records(records)
    print(f"削除しました：{removed['date']} {removed['category']} {removed['amount']:,}円")