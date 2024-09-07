#import PySimpleGUI as sg
import pyocr.builders
from ScreenFunction import pdfFunc
from PIL import Image
import io
import pyocr
import tkinter as tk
import customtkinter as ctk
import ScreenReadFile as sr
import ScreenShowSentence as ss
import ScreenShowImage as si
# import ScreenTransition as st
import ScreenOptionMarker as so
import ScreenPDFFrame as sf
import ScreenToolFrame as st

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

  def get_Marker(self,nowPage):
    self.pdfFrame.sentence.getMarker_Word(nowPage)

  def reconstruction_Marker(self,recPage):
    self.pdfFrame.sentence.highLight_Marker_reconstruction(recPage)

  def get_Option(self):
    return self.option


































# class ScreenConfig:
#   def __init__(self,title):
#     self.title = title
#     self.window = None

#   def createScreen(self):
#     layout =[
#       [sg.Text(background_color="white",key="top")],
#       [sg.Push(background_color="white"),sg.Text("ファイル",text_color="black",background_color="white",key="title"),sg.InputText(key="fileText"),sg.FileBrowse(button_text="ファイル選択",key="pdfFile"),sg.Button("表示する",key="decision"),sg.Push(background_color="white")],
#       [
#         sg.Text(background_color="gray",key="problemStatement"),
#         sg.Image(data=None,key="IMAGE",background_color="white"),
#       ]
#     ]
#     window = sg.Window(self.title,layout,background_color="white",resizable=True,finalize=True,size=(500,800))
#     window.maximize()
#     self.window = window

#   def event_loop(self):
#     pdfController = pdfFunc()
    
#     while True:
#       event, values = self.window.read()
#       if event == "decision":
#         path = values["pdfFile"]
#         pdfController.openPDF(path)
#         img = pdfController.PDF_to_Image(30)
#         pdfController.extractWord(img)
#         #print(text)
#         img.save("outputFile.png",format="png")
#       elif event == sg.WIN_CLOSED:
#         break