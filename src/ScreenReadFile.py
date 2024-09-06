import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc
import ScreenConfig as sc
import ScreenShowSentence as ss
import ScreenShowImage as si

class ReadFileFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master

    # 列の幅を調整する
    self.grid_columnconfigure(0, weight=1)  # ファイルパスエントリーの列が拡張する
    self.grid_columnconfigure(1, weight=1)  # ボタンの列は固定
    self.grid_columnconfigure(2, weight=1)
    self.grid_rowconfigure(0,weight=1)
    
    # ファイルパス表示用のエントリー
    self.file_path_entry = ctk.CTkEntry(self, placeholder_text="File Path",width=600)
    self.file_path_entry.grid(row=0, column=0, sticky="ew")  # 横に広がるように配置

    # エクスプローラーを開くためのボタン
    self.browse_button = ctk.CTkButton(self, text="ファイル選択",font=("meiryo", 12,"bold"),command=self.open_file_explorer)
    self.browse_button.grid(row=0, column=1, padx=5)  # 入力ボックスとの間にスペースを開けて配置

    # 別のボタン
    self.another_button = ctk.CTkButton(self, text="開く",font=("meiryo", 12,"bold"),command=self.open_file_decision)
    self.another_button.grid(row=0, column=2)  # エクスプローラーの隣に配置

    


  def open_file_explorer(self):
    # ファイルダイアログを開いて選択したファイルのパスを入力ボックスに設定
    file_path = filedialog.askopenfilename()
    if file_path:
        self.file_path_entry.delete(0, tk.END)  # 既存のテキストを削除
        self.file_path_entry.insert(0, file_path)  # 新しいファイルパスを挿入
  
  def open_file_decision(self):
    # 選択したファイルのパスを元にファイルを開く
    pdfController = pdfFunc()
    path = self.file_path_entry.get()
    if len(path) != 0:
      # 取得したパスを元にPDFを開く
      self.master.document_len = pdfController.openPDF(path)
      # 取得したpdfを画像に変換する
      imgList = pdfController.PDF_to_Image()
      # 作成したリストをセットする
      self.master.pdfImg = imgList
      # 取得した画像をレイアウト構成に基づいて表示する
      self.master.set_img(imgList[0])
      # 取得した画像から文字を抽出し、レイアウト構成に基づいて表示する
      text = pdfController.extractWord(imgList[0])
      self.master.set_sentence(text)
