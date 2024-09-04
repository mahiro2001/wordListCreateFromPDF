import PySimpleGUI as sg

class ScreenConfig:
  def __init__(self,title):
    self.title = title
    self.window = 0

  def createScreen(self):
    layout =[
      [sg.Push(background_color="white")],
      [sg.Push(background_color="white"),sg.Text("ファイル",text_color="black",background_color="white"),sg.InputText(),sg.FileBrowse(button_text="ファイル選択",key="pdfFile"),sg.Button("表示する"),sg.Push(background_color="white")],
      []
    ]
    window = sg.Window(self.title,layout,background_color="white",resizable=True)
    self.window = window

  def event_loop(self):
    while True:
      event, values = self.window.read()
      if event == sg.WIN_CLOSED:
        break