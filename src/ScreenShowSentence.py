import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc

class ShowSentenceFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)
    self.bind("<Configure>",self.delay_resize_textBox)
    self.grid_propagate(False)
    
    self.sentence = ctk.CTkTextbox(self,wrap="word",font=("meiryo",13,"bold"),fg_color="#242424",text_color="black",state="disabled",padx=0,pady=0)
    self.sentence.grid(row=0, column=0, padx=7.5, pady=7.5,sticky="news")
    self.sentence.bind("<ButtonRelease-1>",self.highLight_Marker_Select)

  # 取得した文字をテキストボックスにセットするための処理
  def set_sentence_config(self,exText):
    self.sentence.configure(state="normal",fg_color="white",corner_radius=0)
    self.sentence.grid_configure(padx=7.5,pady=7.5)
    self.sentence.delete("0.0",ctk.END)
    self.sentence.insert("0.0",exText)

  # ウィンドウサイズに画像を変更する際の遅延処理
  def delay_resize_textBox(self,event):
    self.after(200,self.resizeText)

  # ウィンドウサイズが調整された際のテキストボックスサイズの自動調整処理
  def resizeText(self):
    self.sentence.grid_configure(padx=7.5,pady=7.5)


  # テキストにマーカーを引くための処理
  def highLight_Marker_Select(self,event):
    if self.master.master.get_Option() == "マーカー" and self.sentence.tag_ranges(ctk.SEL):
      markerStart = self.sentence.index(ctk.SEL_FIRST)
      markerEnd = self.sentence.index(ctk.SEL_LAST)
      self.sentence.tag_add("highLight",markerStart,markerEnd)
      self.sentence.tag_config("highLight",background="yellow",foreground="black")

  # 画面移動をした際にマーカー箇所の情報（テキストとその位置）を取得するための処理
  def getMarker_Word(self,nowPage):
    markerList = self.sentence.tag_ranges("highLight")
    positionList = []
    wordList = []
    for index in range(0,len(markerList),2):
      markerTuple = (nowPage,markerList[index:index+2][0],markerList[index:index+2][1])
      if self.check_Unique_positionList(markerTuple):
        positionList.append(markerTuple)
        wordList.append(self.sentence.get(markerList[index:index+2][0],markerList[index:index+2][1]))
    if len(positionList) != 0:
      # wordMarkerPosiionに格納されるデータ例： [[(0,3.19,3.20),(0,4.1,4.5)],[],[(1,3.19,3.20),(1,4.1,4.5)]]
      self.master.master.wordMarkerPosition.append(positionList)
    if len(wordList) != 0:
      self.master.master.wordMarkerList.append(wordList)
    
    # 以下、デバッグ用  
    # print(self.master.wordMarkerPosition)
    # print(self.master.wordMarkerList)
    
  # 既に登録されているポジションかを確認する為の処理
  # False：重複している、True：重複していない
  def check_Unique_positionList(self,markerTuple):
    for markerData in self.master.master.wordMarkerPosition:
      for positionData in markerData:
        if positionData[0] == markerTuple[0] and positionData[1] == markerTuple[1] and positionData[2] == markerTuple[2]:
          return False
    return True

  # ページ移動をした際、以前にマーカーをしていた個所にハイライト（背景色）をつける
  def highLight_Marker_reconstruction(self,recPage):
    for recData in self.master.master.wordMarkerPosition:
      if len(recData) != 0 and recData[0][0] == recPage:
        for positionData in recData:
          markerStart = positionData[1]
          markerEnd = positionData[2]
          self.sentence.tag_add("highLight",markerStart,markerEnd)
          self.sentence.tag_config("highLight",background="yellow",foreground="black")
    
      