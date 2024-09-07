import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc
from PIL import Image 

class ShowImageFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.img = None
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)
    self.grid_propagate(False)

    self.scrollableFrame = ctk.CTkScrollableFrame(self)
    self.scrollableFrame.grid(row=0,column=0,sticky="news")
    self.imageLabel = ctk.CTkLabel(self.scrollableFrame,text="",image=None)
    self.imageLabel.grid(row=0,column=0,sticky="s",padx=0,pady=0)
    self.scrollableFrame._set_scaling(1,1)
    self.imageLabel._set_scaling(1,1)
    self.bind("<Configure>",self.delay_resize)

  # 選択した画像をラベルに貼り付けて表示するための処理
  def updateImage(self,img):
    self.img = img
    w,h = img.size
    width = self.scrollableFrame.winfo_width()
    height = round(h * width / w)
    reImg = ctk.CTkImage(img,size=(width,height))
    self.imageLabel.configure(image=reImg,padx=0,pady=0)
    return height

# ウィンドウサイズに画像を変更する際の遅延処理
  def delay_resize(self,event):
    self.after(200,self.resizeImage)

# ウィンドウサイズが変更された時に呼び出される処理
  def resizeImage(self):
    img = self.img
    if img is not None:
      w,h = img.size
      width = self.scrollableFrame.winfo_width()
      height = round(h*width/w)
      reImg = ctk.CTkImage(img,size=(width,height))
      self.imageLabel.configure(image=reImg,padx=0,pady=0)
      self.scrollableFrame._set_scaling(1,1)
      self.imageLabel._set_scaling(1,1)
