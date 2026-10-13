"""家計簿アプリのメニュー"""
import storage


def main():
    while True:
        print("\n=== 家計簿 ===")
        print("1. 記録を入力")
        print("2. 一覧を表示")
        print("3. 記録を削除")
        print("4. 集計を表示")
        print("5. グラフを表示")
        print("0. 終了")
        choice = input("番号を選んでください：")

        records = storage.load_records()

        if choice == "1":
            print("（フェーズ2で実装）")
        elif choice == "2":
            print("（フェーズ2で実装）")
        elif choice == "3":
            print("（フェーズ2で実装）")
        elif choice == "4":
            print("（フェーズ3で実装）")
        elif choice == "5":
            print("（フェーズ4で実装）")
        elif choice == "0":
            print("終了します")
            break
        else:
            print("0〜5の番号を入力してください")


if __name__ == "__main__":
    main()