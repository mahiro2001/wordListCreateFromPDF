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
  
  def PDF_to_Image(self,page):
    return Image.open(io.BytesIO(self.document.get_page_pixmap(page,dpi=500).tobytes("png")))
  
  # def extractWord(self,img):
  #   tokenizer = Tokenizer()
  #   tools = pyocr.get_available_tools()
  #   tool = tools[0]
  #   text = tool.image_to_string(
  #         img,
  #         lang="jpn",
  #         builder=pyocr.builders.TextBuilder()
  #   )

  #   for token in tokenizer.tokenize(text):
  #     if token.part_of_speech.startswith("名詞"):
  #       print(token.surface)