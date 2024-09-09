import gc
import zlib
import fitz
from PIL import Image
import io
import customtkinter as ctk
import pyocr
from memory_profiler import profile

# 【同期処理】
# pdfファイルデータを取得するための処理
def openPDF_top_document(path):
    document = fitz.open(path)
    return document


# 【同期処理関連】
# 画像から文字を抽出するための処理Ⅿ
def extractWord(img):
  tools = pyocr.get_available_tools()
  tool = tools[0]
  imgL = img.convert("L")
  text = tool.image_to_string(
        imgL,
        lang="jpn",
        builder=pyocr.builders.TextBuilder()
  )
  del imgL
  return text

class pdfFunc():
  def __init__(self):
    self.document_len = None

  # 【同期処理】
  # PDFデータを画像に変換するための処理
  def PDF_to_Image(self,path):
    # pdfを読みこむ
    document = openPDF_top_document(path)
    # 指定された開始・終了位置をそれぞれ格納
    self.document_len = len(document)
    # ページ番号と画像データをまとめたリストをさらにまとめるリスト[[ページ番号,画像データ],[ページ番号,画像データ]]
    imgList = []
    # 取得した画像データから文字を抽出し、格納するためのリスト
    wordList = []
    # 指定した範囲のpdfを画像に変換し、ページ数と画像データを紐づけ、リストに追加する
    progress_dialog = ctk.CTkToplevel()
    progress_dialog.grab_set()
    progress_dialog.focus_set()
    progress_dialog.title("読み込み中...")
    progress_dialog.geometry("400x200+200+200")
    progress_dialog.attributes("-topmost",True)
    progress_dialog.grid_columnconfigure(0, weight=1)
    progress_dialog.grid_rowconfigure(0,weight=1)
    progress_dialog.grid_rowconfigure(1,weight=1)
    progressbar = ctk.CTkProgressBar(progress_dialog,width=200,height=15)
    progressbar.grid(row=0,column=0,sticky="ew",padx=30)
    progressLabel = ctk.CTkLabel(progress_dialog,text=" ")
    progressLabel.grid(row=1,column=0,sticky="news")
    progressCount = 0
    progressbar.set(0.0)
    for page in range(self.document_len):
      img_binary = io.BytesIO(document.get_page_pixmap(page,dpi=500).tobytes("png"))
      img_binary_zip = zlib.compress(img_binary.getvalue())
      img = Image.open(img_binary)
      text = extractWord(img)
      imgList.append(img_binary_zip)
      wordList.append(text)
      progressCount += 1
      progressLabel.configure(text=f"{progressCount}/{self.document_len}")
      progressbar.set(progressCount/self.document_len)
      progressbar.update()
    progress_dialog.destroy()
    document.close()
    return imgList,wordList