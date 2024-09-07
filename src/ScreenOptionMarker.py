import customtkinter as ctk

class ScreenOptionFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)

    self.optionmenu = ctk.CTkOptionMenu(self,values=["マーカー","消しゴム"],font=("meiryo",12,"bold"),command=self.option_Change)
    self.optionmenu.grid(row=0,column=0,sticky="ew",padx=5)

  def option_Change(self,event):
    self.master.master.option = self.optionmenu.get()