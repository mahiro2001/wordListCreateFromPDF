import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc

class ScreenTransitionFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)

    self.nextButton = ctk.CTkButton(self,text="次のページ",height=20,font=("meiryo",12,"bold"),command=self.goNextPage)
    self.nextButton.grid(row=0,column=0,pady=(10,5),sticky="news",padx=5)
    self.backButton = ctk.CTkButton(self,text="前のページ",height=20,font=("meiryo",12,"bold"),command=self.goBackPage)
    self.backButton.grid(row=1,column=0,pady=(5,10),sticky="news",padx=5)

  def goNextPage(self):
    # 現在の表示しているpdfのページを取得
    nowPage = self.master.master.page
    # pdfの最大ページ数より現在のページが小さければ処理を行う
    if self.master.master.document_len - 1 > nowPage:
      nextPage = nowPage + 1
      self.master.master.set_page(nextPage)
      # 取得した画像をレイアウト構成に基づいて表示する
      self.master.master.set_img(self.master.master.pdfImg[nextPage])
      # 取得した問題をレイアウト構成に基づいて表示する
      self.master.master.set_sentence(self.master.master.wordList[nextPage])
      # 以前マーカーをしていた箇所にハイライトをつけるための処理
      self.master.master.reconstruction_Marker(nextPage)
      

  def goBackPage(self):
    # 現在の表示しているpdfのページを取得
    nowPage = self.master.master.page
    # pdfの最小のページ数より現在のページ数が大きければ処理を行う
    if nowPage > 0:
      backPage = nowPage - 1
      self.master.master.set_page(backPage)
      # 取得した画像をレイアウト構成に基づいて表示する
      self.master.master.set_img(self.master.master.pdfImg[backPage])
      # 取得した問題をレイアウト構成に基づいて表示する
      self.master.master.set_sentence(self.master.master.wordList[backPage])
      # 以前マーカーをしていた箇所にハイライトをつけるための処理
      self.master.master.reconstruction_Marker(backPage)