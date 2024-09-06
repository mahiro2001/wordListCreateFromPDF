import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from ScreenFunction import pdfFunc

class ToolTableFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_rowconfigure(0, weight=1)

    self.nextButton = ctk.CTkButton(self,width=50,height=40,text="次のページ",font=("meiryo",12,"bold"))
    self.nextButton.grid(row=0,column=1,padx=(5,10),pady=5,sticky="ew")
    self.backButton = ctk.CTkButton(self,width=50,height=40,text="前のページ",font=("meiryo",12,"bold"))
    self.backButton.grid(row=0,column=0,padx=(10,5),pady=5,sticky="ew")