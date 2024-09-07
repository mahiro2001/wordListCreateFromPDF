import customtkinter as ctk
import ScreenShowSentence as ss
import ScreenShowImage as si

class ScreenPDFFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_propagate(False)
    
    self.sentence = ss.ShowSentenceFrame(master=self)
    self.sentence.grid(row=0,column=0,sticky="news")
    self.pdfImage = si.ShowImageFrame(master=self)
    self.pdfImage.grid(row=0,column=1,sticky="news")