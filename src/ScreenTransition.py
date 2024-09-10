import customtkinter as ctk

class ScreenTransitionFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)
    self.grid_propagate(False)

    self.nextButton = ctk.CTkButton(self,text="次のページ",height=20,width=100,font=("meiryo",12,"bold"),command=self.goNextPage)
    self.nextButton.grid(row=0,column=0,pady=(10,5),sticky="ns",padx=5)
    self.backButton = ctk.CTkButton(self,text="前のページ",height=20,width=100,font=("meiryo",12,"bold"),command=self.goBackPage)
    self.backButton.grid(row=1,column=0,pady=(5,10),sticky="ns",padx=5)

  def goNextPage(self):
    if self.master.master.document_len != None:
      # 現在の表示しているpdfのページを取得
      nowPage = self.master.master.page
      # pdfの最大ページ数より現在のページが小さければ処理を行う
      if self.master.master.document_len - 1 > nowPage:
        if self.master.master.text_change_flag:
          self.master.master.call_csv_override(nowPage)
          self.master.master.text_change_flag = False
        nextPage = nowPage + 1
        self.master.master.set_page(nextPage)
        # 取得した画像をレイアウト構成に基づいて表示する
        self.master.master.set_img(self.master.master.read_csv_to_List_Images(self.master.master.img_path,nextPage))
        # 取得した問題をレイアウト構成に基づいて表示する
        self.master.master.set_sentence(self.master.master.read_csv_to_List(self.master.master.text_path,nextPage))
        # 以前マーカーをしていた箇所にハイライトをつけるための処理
        self.master.master.reconstruction_Marker(nextPage)
    else:
      error_dialog = ctk.CTkToplevel()
      error_dialog.iconbitmap("favicon.ico")
      error_dialog.title("警告")
      error_dialog.geometry("300x100+500+400")
      error_dialog.attributes("-topmost",True)
      error_dialog.grab_set()
      error_dialog.focus_set()
      error_dialog.grid_columnconfigure(0, weight=1)
      error_dialog.grid_rowconfigure(0,weight=1)
      errorText = ctk.CTkLabel(error_dialog,text="PDFファイルを選択してください",font=("meiryo", 12,"bold"),text_color="red")
      errorText.grid(row=0,column=0)
      self.master.master.wait_window(error_dialog)
      

  def goBackPage(self):
    if self.master.master.document_len != None:
      # 現在の表示しているpdfのページを取得
      nowPage = self.master.master.page
      # pdfの最小のページ数より現在のページ数が大きければ処理を行う
      if nowPage > 0:
        if self.master.master.text_change_flag:
          self.master.master.call_csv_override(nowPage)
          self.master.master.text_change_flag = False
        backPage = nowPage - 1
        self.master.master.set_page(backPage)
        # 取得した画像をレイアウト構成に基づいて表示する
        self.master.master.set_img(self.master.master.read_csv_to_List_Images(self.master.master.img_path,backPage))
        # 取得した問題をレイアウト構成に基づいて表示する
        self.master.master.set_sentence(self.master.master.read_csv_to_List(self.master.master.text_path,backPage))
        # 以前マーカーをしていた箇所にハイライトをつけるための処理
        self.master.master.reconstruction_Marker(backPage)
    else:
      error_dialog = ctk.CTkToplevel()
      error_dialog.iconbitmap("favicon.ico")
      error_dialog.title("警告")
      error_dialog.geometry("300x100+500+400")
      error_dialog.attributes("-topmost",True)
      error_dialog.grab_set()
      error_dialog.focus_set()
      error_dialog.grid_columnconfigure(0, weight=1)
      error_dialog.grid_rowconfigure(0,weight=1)
      errorText = ctk.CTkLabel(error_dialog,text="PDFファイルを選択してください",font=("meiryo", 12,"bold"),text_color="red")
      errorText.grid(row=0,column=0)
      self.master.master.wait_window(error_dialog)