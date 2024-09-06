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

FONT_TYPE = "meiryo"

class Application(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.fonts = (FONT_TYPE, 15,"bold")
    self.geometry("1000x600+0+0")
    self.minsize(1000,600)
    self.title("WordListCreateFromPDF")
    self.image = None
    self.height = self.winfo_screenheight()
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_columnconfigure(2,weight=1)
    self.grid_columnconfigure(3,weight=1)
    self.grid_rowconfigure(0,weight=1)
    self.grid_rowconfigure(1,weight=3)
    self.grid_rowconfigure(2,weight=1)
    self.setup_form()

  def setup_form(self):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    self.readFileFrame = sr.ReadFileFrame(master=self)
    self.readFileFrame.grid(row=0,column=0,columnspan=4, padx=20, pady=5)
    self.showImage = si.ShowImageFrame(master=self)
    self.showImage.grid(row=1,column=2,columnspan=2,padx=(2,20),sticky="news")
    self.showSentence = ss.ShowSentenceFrame(master=self)
    self.showSentence.grid(row=1,column=0,columnspan=2, padx=(20,2),sticky="news")
    

 # 画像が選択、確定された場合の処理
 # pdfから読み取った画像を表示する
  def set_img(self,img):
    self.img = img
    self.showImage.updateImage(img)

  # 画像が選択、確定された場合の処理
  # テキストボックスの書き込みを可能にする
  def set_sentence(self,text):
    self.showSentence.set_sentence_config(text)









































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