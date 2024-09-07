import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc

class ToolTableFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_rowconfigure(0, weight=1)

    self.nextButton = ctk.CTkButton(self,width=50,height=40,text="次のページ",font=("meiryo",12,"bold"),command=self.goNextPage)
    self.nextButton.grid(row=0,column=1,padx=(5,10),pady=5,sticky="ew")
    self.backButton = ctk.CTkButton(self,width=50,height=40,text="前のページ",font=("meiryo",12,"bold"),command=self.goBackPage)
    self.backButton.grid(row=0,column=0,padx=(10,5),pady=5,sticky="ew")

  def goNextPage(self):
    # 現在の表示しているpdfのページを取得
    nowPage = self.master.page
    # マーカーが引かれた文字とその位置を保持するための処理
    self.master.get_Marker(nowPage)
    # pdfの最大ページ数より現在のページが小さければ処理を行う
    if self.master.document_len - 1 > nowPage:
      nextPage = nowPage + 1
      self.master.set_page(nextPage)
      # 取得した画像をレイアウト構成に基づいて表示する
      self.master.set_img(self.master.pdfImg[nextPage])
      # 取得した問題をレイアウト構成に基づいて表示する
      self.master.set_sentence(self.master.wordList[nextPage])
      

  def goBackPage(self):
    # 現在の表示しているpdfのページを取得
    nowPage = self.master.page
    # マーカーが引かれた文字とその位置を保持するための処理
    self.master.get_Marker(nowPage)
    # pdfの最小のページ数より現在のページ数が大きければ処理を行う
    if nowPage > 0:
      backPage = nowPage - 1
      self.master.set_page(backPage)
      # 取得した画像をレイアウト構成に基づいて表示する
      self.master.set_img(self.master.pdfImg[backPage])
      # 取得した問題をレイアウト構成に基づいて表示する
      self.master.set_sentence(self.master.wordList[backPage])