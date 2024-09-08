from concurrent.futures import ProcessPoolExecutor
import fitz
from PIL import Image
import io
import customtkinter as ctk
import pyocr

# 【非同期処理】
# 指定したページのpdfを読みこみ、pdfを画像に変換後、リストで保存する処理
def PDF_to_Image_topFunc(rangeLen,path):
  # pdfを読みこむ
  document = openPDF_top_document(path)
  # 指定された開始・終了位置をそれぞれ格納
  start,end = rangeLen
  # ページ番号と画像データをまとめたリストをさらにまとめるリスト[[ページ番号,画像データ],[ページ番号,画像データ]]
  imgList = []
  # 取得した画像データから文字を抽出し、格納するためのリスト
  wordList = []
  # 指定した範囲のpdfを画像に変換し、ページ数と画像データを紐づけ、リストに追加する
  for page in range(start,end):
    # pdfのページ情報と画像のバイナリデータを紐づける為のリスト[ページ番号,画像データ]
    pdfList = []
    textList = []
    pdfList.append(page)
    textList.append(page)
    img = Image.open(io.BytesIO(document.get_page_pixmap(page,dpi=500).tobytes("png")))
    text = extractWord(img)
    pdfList.append(img)
    textList.append(text)
    imgList.append(pdfList)
    wordList.append(textList)
  return imgList,wordList

# 【非同期処理】
# pdfファイルデータを取得するための処理
def openPDF_top_document(path):
    document = fitz.open(path)
    return document

# 【非同期処理関連】
# pdfの総ページ数を取得するための処理
def openPDF_top_document_len(path):
    document = fitz.open(path)
    document_len = len(document)
    return document_len

# 【非同期処理関連】
# 並行処理するためにpdfページの処理範囲を決めるための処理
def division_page_top(document_len):
  threadNum = 1
  avgPage = document_len / threadNum
  preNum = 0
  lenList = []
  for num in range(document_len):
    if num != 0 and num % avgPage == 0:
      lenList.append((preNum,num+1))
      preNum = num + 1
  if len(lenList) != threadNum:
    lenList.append((preNum,document_len))
  return lenList

# 【非同期処理関連】
# 画像データが格納されているリストを結合するための処理
def union_List(resList):
  imgAllList = []
  textAllList = []
  for index in range(len(resList)):
    imgList, textList = resList[index].result()
    imgAllList += imgList
    textAllList += textList
  return imgAllList,textAllList

# 【非同期処理関連】
# 抽出した画像データをページ番号と合わせてまとめているリストのページ番号を取り除いたリストを作成するための処理
def extract_PageNum_AllList(resTuple):
  imgList,textList = resTuple
  reImgList = []
  reTextList = []

  for imageInfo in imgList:
    reImgList.append(imageInfo[1])
  
  for textInfo in textList:
    reTextList.append(textInfo[1])

  return reImgList,reTextList 



# 【非同期処理関連】
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
  return text



# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================

class pdfFunc():
  def __init__(self):
    self.document_len = None
  
  
  # 【非同期処理関連】
  # 非同期処理をするメソッドを呼び出すための処理
  def multiprocess_pdf_to_image(self,path):
    # pdfの総ページ数を取得
    document_len = openPDF_top_document_len(path)
    self.document_len = document_len
    # pdfの総ページ数からどの位置で分割するかを決める処理
    divisionList = division_page_top(document_len)
    # 複数の非同期処理の結果を格納するためのリスト
    resList = []
    # 非同期処理、PDF_to_Image_topFuncメソッドを非同期で指定したページごとで処理を行う
    with ProcessPoolExecutor(max_workers=1) as executor:
      for divisionInfo in divisionList:
        resList.append(executor.submit(PDF_to_Image_topFunc,divisionInfo,path))
    return extract_PageNum_AllList(union_List(resList))
  
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================

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
      # pdfのページ情報と画像のバイナリデータを紐づける為のリスト[ページ番号,画像データ]
      # pdfList = []
      # textList = []
      # pdfList.append(page)
      # textList.append(page)
      img = Image.open(io.BytesIO(document.get_page_pixmap(page,dpi=500).tobytes("png")))
      text = extractWord(img)
      # pdfList.append(img)
      # textList.append(text)
      imgList.append(img)
      wordList.append(text)
      progressCount += 1
      progressLabel.configure(text=f"{progressCount}/{self.document_len}")
      progressbar.set(progressCount/self.document_len)
      progressbar.update()
    # self.master.wait_window(progress_dialog)
    progress_dialog.destroy()
    return imgList,wordList