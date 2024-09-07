import customtkinter as ctk

class ScreenUndecideFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)
    self.grid_propagate(False)

    self.undecide = ctk.CTkLabel(self,text=" ",fg_color="#333333")
    self.undecide.grid(row=0,column=0,padx=0,pady=0,sticky="news")