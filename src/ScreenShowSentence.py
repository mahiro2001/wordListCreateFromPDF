import csv
import customtkinter as ctk
from tkinter import END

class ShowSentenceFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.change_flag_count = 0

    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)
    self.bind("<Configure>",self.delay_resize_textBox)
    self.grid_propagate(False)
    
    self.sentence = ctk.CTkTextbox(self,wrap="word",font=("meiryo",13,"bold"),fg_color="#242424",text_color="black",state="disabled",padx=0,pady=0)
    self.sentence.grid(row=0, column=0, padx=7.5, pady=7.5,sticky="news")
    self.sentence.bind("<ButtonRelease-1>",self.highLight_Marker_Select)
    self.sentence.bind("<Button-1>",self.highLight_Marker_remove)
    self.sentence.bind("<KeyRelease>",self.change_flag_text)

  # 文字に変更があった場合の処理
  def change_flag_text(self,event):
    if self.change_flag_count == 0:
      self.master.master.text_change_flag = True
  
  def text_csv_override(self,file_path,page):
    with open(file_path, mode="r", encoding="utf-8") as file:
      # テキスト情報格納しているcsvファイルを取得
      reader = csv.reader(file)
      # 変更した文章を代入するためにリスト化
      reader = list(reader)
      # 変更した文章をすべて取得してくる
      temp_str = self.sentence.get("0.0",END)
      # 変更した文章をリスト化する
      temp = []
      temp.append(temp_str)
      # 変更したページの文章情報を上書きする
      reader[page] = temp
    # csvに上書きする
    with open(file_path,mode="w",newline="",encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerows(reader)
        

  # 取得した文字をテキストボックスにセットするための処理
  def set_sentence_config(self,exText):
    self.sentence.configure(state="normal",fg_color="white",corner_radius=0)
    self.sentence.grid_configure(padx=7.5,pady=7.5)
    self.sentence.delete("0.0",ctk.END)
    self.sentence.insert("0.0",exText[0])

  # ウィンドウサイズに画像を変更する際の遅延処理
  def delay_resize_textBox(self,event):
    self.after(200,self.resizeText)

  # ウィンドウサイズが調整された際のテキストボックスサイズの自動調整処理
  def resizeText(self):
    self.sentence.grid_configure(padx=7.5,pady=7.5)


  # テキストにマーカーを引くための処理
  def highLight_Marker_Select(self,event):
    if self.master.master.get_Option() == "マーカー" and self.sentence.tag_ranges(ctk.SEL):
      nowPage = self.master.master.page
      markerStart = self.sentence.index(ctk.SEL_FIRST)
      markerEnd = self.sentence.index(ctk.SEL_LAST)
      self.sentence.tag_add("highLight",markerStart,markerEnd)
      self.sentence.tag_config("highLight",background="yellow",foreground="black")
      markerTuple = (nowPage,markerStart,markerEnd)
      if self.check_Unique_positionList(markerTuple):
        self.master.master.wordMarkerPosition.append(markerTuple)
        self.master.master.wordMarkerList.append(self.sentence.get(markerStart,markerEnd))
      
  # 既に登録されているポジションかを確認する為の処理
  # False：重複している、True：重複していない
  def check_Unique_positionList(self,markerTuple):
    for positionData in self.master.master.wordMarkerPosition:
        if positionData[0] == markerTuple[0] and positionData[1] == markerTuple[1] and positionData[2] == markerTuple[2]:
          return False
    return True

  # ページ移動をした際、以前にマーカーをしていた個所にハイライト（背景色）をつける
  def highLight_Marker_reconstruction(self,recPage):
    for recData in self.master.master.wordMarkerPosition:
      if recData[0] == recPage:
        markerStart = str(recData[1])
        markerEnd = str(recData[2])
        self.sentence.tag_add("highLight",markerStart,markerEnd)
        self.sentence.tag_config("highLight",background="yellow",foreground="black")
    
  # マーカーされた箇所を取り消すための処理
  def highLight_Marker_remove(self,event):
    if self.master.master.get_Option() == "消しゴム":
      nowPage = self.master.master.page
      selectPosition = self.sentence.index(f"@{event.x},{event.y}")
      for positionData in self.master.master.wordMarkerPosition:
          mark_Start_Num = str(positionData[1]).split(".")
          mark_End_Num = str(positionData[2]).split(".")
          selectNum = str(selectPosition).split(".")
          if positionData[0] == nowPage and (float(mark_Start_Num[0]) <= float(selectNum[0]) and float(mark_Start_Num[1]) <= float(selectNum[1])) and (float(mark_End_Num[0]) >= float(selectNum[0]) and float(mark_End_Num[1]) >= float(selectNum[1])):
            self.master.master.wordMarkerPosition.remove((nowPage,positionData[1],positionData[2]))
            self.master.master.wordMarkerList.remove(self.sentence.get(positionData[1],positionData[2]))
            self.sentence.tag_remove("highLight",positionData[1],positionData[2])