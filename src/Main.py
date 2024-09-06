import ScreenConfig

if __name__ == "__main__":
  screenConfig = ScreenConfig.Application()
  screenConfig.mainloop()

# # ScreenConfigクラスのオブジェクトの作成
# screenConfig = ScreenConfig("CreateWordList")

# # 画面表示をするための設定
# # 第一引数：アプリ名, 第二引数：画面情報（初期値は0とする）
# screenConfig.createScreen()

# # 画面を表示し、入出力を受け続ける
# # windowの「×」でloopを抜け、アプリが終了する
# screenConfig.event_loop()
