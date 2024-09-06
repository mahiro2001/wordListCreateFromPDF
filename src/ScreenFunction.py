import fitz
from PIL import Image
import io
import pyocr
from janome.tokenizer import Tokenizer

class pdfFunc:
  def __init__(self):
    self.path = None
    self.document = None
    self.document_len = None
  
  def openPDF(self,path):
    self.document = fitz.open(path)
    self.document_len = len(self.document)
    return self.document_len

  # PDFを読みこんだタイミングで全てのページを読みこみ、リストで保存する処理
  def PDF_to_Image(self):
    imgList = []
    for page in range(self.document_len):
      imgList.append(Image.open(io.BytesIO(self.document.get_page_pixmap(page,dpi=500).tobytes("png"))))
    return imgList
  
  # 画像から文字を抽出するための処理Ⅿ
  def extractWord(self,img):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    text = tool.image_to_string(
          img,
          lang="jpn",
          builder=pyocr.builders.TextBuilder()
    )
    return text