import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
import ScreenFunction as sf
import csv
import os
import base64

csv.field_size_limit(10**8)

# csvファイルに出力するための処理（テキストデータ）
def write_list_to_csv(file_path,data):
  with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# csvファイルに出力するための処理（画像データ）
def write_list_to_csv_images(file_path,data):
  with open(file_path, mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# 画像データをBase64にエンコードするための処理
def encode_base64_image(data):
  imageData = []
  for binaryData in data:
    imageData.append(base64.b64encode(binaryData).decode("utf-8"))
  return imageData

class ReadFileFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master

    # 列の幅を調整する
    self.grid_columnconfigure(0, weight=1)  # ファイルパスエントリーの列が拡張する
    self.grid_columnconfigure(1, weight=1)  # ボタンの列は固定
    self.grid_columnconfigure(2, weight=1)
    self.grid_columnconfigure(3, weight=1)
    self.grid_rowconfigure(0,weight=1)
    
    # ファイルパス表示用のエントリー
    self.file_path_entry = ctk.CTkEntry(self, placeholder_text="PDFファイルを選択してください",width=600,font=("meiryo", 12,"bold"))
    self.file_path_entry.grid(row=0, column=0, sticky="ew")  # 横に広がるように配置

    # エクスプローラーを開くためのボタン
    self.browse_button = ctk.CTkButton(self, text="ファイル選択",font=("meiryo", 12,"bold"),command=self.open_file_explorer)
    self.browse_button.grid(row=0, column=1, padx=5)  # 入力ボックスとの間にスペースを開けて配置

    # 別のボタン
    self.another_button = ctk.CTkButton(self, text="開く",font=("meiryo", 12,"bold"),command=self.open_file_decision)
    self.another_button.grid(row=0, column=2)  # エクスプローラーの隣に配置

    # csvファイルを出力するためのボタン
    self.csv_output_button = ctk.CTkButton(self, text="単語リストを作成",font=("meiryo", 12,"bold"),command=self.output_CSVFile)
    self.csv_output_button.grid(row=0, column=3,padx=(5,0))

  def open_file_explorer(self):
    # ファイルダイアログを開いて選択したファイルのパスを入力ボックスに設定
    file_path = filedialog.askopenfilename(title="PDFファイルを選択",filetypes=[("PDF files","*.pdf")])
    if file_path:
        self.file_path_entry.delete(0, tk.END)  # 既存のテキストを削除
        self.file_path_entry.insert(0, file_path)  # 新しいファイルパスを挿入
  
  def open_file_decision(self):
    # 選択したファイルのパスを元にファイルを開く
    pdfController = sf.pdfFunc()
    path = self.file_path_entry.get()
    if len(path) != 0:
      if self.master.document_len != 0:
        self.master.initData()
      # pdfから画像に変換する処理を並列で行う 
      mulitiProcess_resultTuple = pdfController.PDF_to_Image(path)
      mulitiProcess_resultImgList, mulitiProcess_resultTextList = mulitiProcess_resultTuple
      # 文章のテキストデータを2次元配列に変換
      data = [[word] for word in mulitiProcess_resultTextList]
      mulitiProcess_resultTextList = None
      write_list_to_csv("wordList.csv",data)

      #pdfの総ページ数を管理側のdocument_lenに格納
      self.master.document_len = pdfController.document_len 
      
      # PDF画像を2次元配列に変換
      imageData = [[img] for img in encode_base64_image(mulitiProcess_resultImgList)]
      mulitiProcess_resultImgList = None
      write_list_to_csv_images("imgList.csv",imageData)
      
      # 取得した画像をレイアウト構成に基づいて表示する
      self.master.set_img(self.master.read_csv_to_List_Images("imgList.csv",0))
      
      # 取得した問題集から1ページ目の文字を表示する
      self.master.set_sentence(self.master.read_csv_to_List("wordList.csv",0))
    else:
      error_dialog = ctk.CTkToplevel()
      error_dialog.grab_set()
      error_dialog.focus_set()
      error_dialog.title("警告")
      error_dialog.geometry("300x100+500+400")
      error_dialog.attributes("-topmost",True)
      error_dialog.grid_columnconfigure(0, weight=1)
      error_dialog.grid_rowconfigure(0,weight=1)
      errorText = ctk.CTkLabel(error_dialog,text="PDFファイルを選択してください",font=("meiryo", 12,"bold"),text_color="red")
      errorText.grid(row=0,column=0)
      self.master.wait_window(error_dialog)

  # CSVファイルを出力するための処理
  def output_CSVFile(self):
    data = self.master.wordMarkerList
    if len(data) != 0:
      file_path = os.path.normpath(filedialog.askdirectory(title="保存先を選択"))
      if len(file_path) != 0:
        file_path = os.path.join(file_path,"createWordList.csv")
        # 2次元配列に変換
        data = [[word] for word in data]
        with open(file_path, mode="w", newline="", encoding="Shift-JIS") as file:
          writer = csv.writer(file)
          writer.writerows(data)

        error_dialog = ctk.CTkToplevel()
        error_dialog.grab_set()
        error_dialog.focus_set()
        error_dialog.title("ダウンロード完了")
        error_dialog.geometry("400x200+200+300")
        error_dialog.attributes("-topmost",True)
        error_dialog.grid_columnconfigure(0, weight=1)
        error_dialog.grid_rowconfigure(0,weight=1)
        errorText = ctk.CTkLabel(error_dialog,text="ダウンロードが完了しました！",font=("meiryo", 12,"bold"),text_color="Green")
        errorText.grid(row=0,column=0)
        self.master.wait_window(error_dialog)
    else:
      error_dialog = ctk.CTkToplevel()
      error_dialog.grab_set()
      error_dialog.focus_set()
      error_dialog.title("警告")
      error_dialog.geometry("300x100+500+400")
      error_dialog.attributes("-topmost",True)
      error_dialog.grid_columnconfigure(0, weight=1)
      error_dialog.grid_rowconfigure(0,weight=1)
      errorText = ctk.CTkLabel(error_dialog,text="1つ以上の単語を選択してください",font=("meiryo", 12,"bold"),text_color="red")
      errorText.grid(row=0,column=0)
      self.master.wait_window(error_dialog)
  