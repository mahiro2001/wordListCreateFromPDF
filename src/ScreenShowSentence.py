import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc

class ShowSentenceFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)
    self.bind("<Configure>",self.delay_resize_textBox)

    self.sentence = ctk.CTkTextbox(self,wrap="word",font=("meiryo",11,"bold"),fg_color="#333333",text_color="black",state="disabled",padx=13,pady=5)
    self.sentence.grid(row=0, column=0, padx=0, pady=0,sticky="news")

  def set_sentence_config(self,exText):
    self.sentence.configure(state="normal",fg_color="white",corner_radius=0)
    self.sentence.grid_configure(padx=10,pady=10)
    self.sentence.insert("0.0",exText)

  # ウィンドウサイズに画像を変更する際の遅延処理
  def delay_resize_textBox(self,event):
    self.after(200,self.resizeText)

  def resizeText(self):
    self.sentence.grid_configure(padx=10,pady=10)
