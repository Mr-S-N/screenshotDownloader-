from pytesseract import image_to_string
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def textFromImg(path):
    return image_to_string(Image.open(path))

