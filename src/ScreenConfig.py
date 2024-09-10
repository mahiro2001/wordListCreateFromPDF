import csv
import zlib
import customtkinter as ctk
import ScreenReadFile as sr
import ScreenPDFFrame as sf
import ScreenToolFrame as st
import base64

FONT_TYPE = "meiryo"

class Application(ctk.CTk):
  def __init__(self):
    super().__init__()

    # ウィンドウの書記設定
    self.fonts = (FONT_TYPE, 15,"bold")
    self.geometry("1000x600+0+0")
    self.minsize(1000,600)
    self.title("WordListCreateFromPDF")
    self.image = None
    self.height = self.winfo_screenheight()
    self.grid_propagate(False)

    # PDF情報の保持フィールド
    # アプリ上で表示しているページ数を保持
    self.page = 0
    # PDFの総ページ数を格納するための変数
    self.document_len = None
    # 抽出された文章中からマーカーが引かれた位置をまとめるリスト
    self.wordMarkerPosition = []
    # 抽出された文字をまとめるリスト
    self.wordMarkerList = []
    # 抽出された文章を保存しているcsvファイルのパス情報
    self.text_path = None
    # 抽出された画像を保存しているcsvファイルのパス情報
    self.img_path = None
    # 文章に変更があるかを判断するためのフラグ
    self.text_change_flag = False

    # オプションの状態を保持する変数
    self.option = "マーカー"

    # レイアウトの構成設定
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)
    self.grid_rowconfigure(1,weight=10)
    self.grid_rowconfigure(2,weight=0)
    self.setup_form()

  def setup_form(self):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    # 上段
    self.readFileFrame = sr.ReadFileFrame(master=self)
    self.readFileFrame.grid(row=0,column=0, padx=20, pady=5)
    # 中段  
    self.pdfFrame = sf.ScreenPDFFrame(master=self)
    self.pdfFrame.grid_propagate(False)
    self.pdfFrame.grid(row=1,column=0,padx=20,pady=5,sticky="news")
    # 下段
    self.toolFrame = st.ScreenToolFrame(master=self,height=100)
    self.toolFrame.grid_propagate(False)
    self.toolFrame.grid(row=2,column=0,padx=20,pady=5,sticky="news")
    

 # 画像が選択、確定された場合の処理
 # pdfから読み取った画像を表示する
  def set_img(self,img):
    self.img = img
    self.pdfFrame.pdfImage.updateImage(img)

  # 画像が選択、確定された場合の処理
  # テキストボックスの書き込みを可能にする
  def set_sentence(self,text):
    self.pdfFrame.sentence.set_sentence_config(text)

  def set_page(self,page):
    self.page = page

  def reconstruction_Marker(self,recPage):
    self.pdfFrame.sentence.highLight_Marker_reconstruction(recPage)

  def get_Option(self):
    return self.option

  def set_ErrorText(self,text):
    self.toolFrame.errorText.set_Text(text)
  
  def initData(self):
    # PDF情報の保持フィールド
    # アプリ上で表示しているページ数を保持
    self.page = 0
    # PDFを画像変換した情報を保持
    self.pdfImg = None
    # PDFの総ページ数を格納するための変数
    self.document_len = None
    # PDFから抽出した文章をまとめているリスト
    self.wordList = None
    # 抽出された文章中からマーカーが引かれた位置をまとめるリスト
    self.wordMarkerPosition = []
    # 抽出された文字をまとめるリスト
    self.wordMarkerList = []

    # オプションの状態を保持する変数
    self.option = self.get_Option()

  # csvファイルから特定の行のデータを取得するための処理
  def read_csv_to_List(self,file_path,page):
    with open(file_path, mode="r", encoding="utf-8") as file:
      reader = csv.reader(file)
      for nowPage,data in enumerate(reader,start=1):
        if nowPage == page+1:
          return data
  
  # csvファイルから画像データのバイナリデータを読み出すための処理
  def read_csv_to_List_Images(self,file_path,page):
      with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        for nowPage,data in enumerate(reader, start=1):
          if nowPage == page+1:
            compress_data = base64.b64decode(data[0])
            return zlib.decompress(compress_data)
          
  # テキストボックス内の文章に変更があった場合の処理
  # 変更箇所をcsvに上書きするための処理を呼び出す
  def call_csv_override(self,page):
    self.pdfFrame.sentence.text_csv_override(self.text_path,page)