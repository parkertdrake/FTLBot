import pytesseract
import Utility
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print pytesseract.image_to_string(Image.open('test.jpg'))


pixel = [240, 240, 240]
print Utility.color(pixel)