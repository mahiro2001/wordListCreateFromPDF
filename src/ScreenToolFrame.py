import customtkinter as ctk
import ScreenTransition as st
import ScreenOptionMarker as so
import ScreenUndecide as su

class ScreenToolFrame(ctk.CTkFrame):
  def __init__(self,master, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_columnconfigure(2,weight=1)
    self.grid_columnconfigure(3,weight=1)
    self.grid_columnconfigure(4,weight=1)
    self.grid_columnconfigure(5,weight=1)
    self.grid_columnconfigure(6,weight=1)
    self.grid_columnconfigure(7,weight=1)
    self.grid_rowconfigure(0,weight=1)
    self.grid_propagate(False)

    self.undecided = su.ScreenUndecideFrame(master=self)
    self.undecided.grid_propagate(False)
    self.undecided.grid(row=0,column=0,padx=0,pady=0,sticky="news")

    self.undecided = su.ScreenUndecideFrame(master=self)
    self.undecided.grid_propagate(False)
    self.undecided.grid(row=0,column=1,padx=0,pady=0,sticky="news")

    self.undecided = su.ScreenUndecideFrame(master=self)
    self.undecided.grid_propagate(False)
    self.undecided.grid(row=0,column=2,padx=0,pady=0,sticky="news")

    self.undecided = su.ScreenUndecideFrame(master=self)
    self.undecided.grid_propagate(False)
    self.undecided.grid(row=0,column=3,padx=0,pady=0,sticky="news")

    self.undecided = su.ScreenUndecideFrame(master=self)
    self.undecided.grid_propagate(False)
    self.undecided.grid(row=0,column=4,padx=0,pady=0,sticky="news")

    self.undecided = su.ScreenUndecideFrame(master=self)
    self.undecided.grid_propagate(False)
    self.undecided.grid(row=0,column=5,padx=0,pady=0,sticky="news")

    self.optionMenu = so.ScreenOptionFrame(master=self)
    self.optionMenu.grid_propagate(False)
    self.optionMenu.grid(row=0,column=6,padx=0,pady=0,sticky="news")

    self.pageTransitionButton = st.ScreenTransitionFrame(master=self)
    self.pageTransitionButton.grid_propagate(False)
    self.pageTransitionButton.grid(row=0,column=7,padx=0,pady=0,sticky="news")
    
    