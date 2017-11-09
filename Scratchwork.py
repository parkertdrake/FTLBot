import pytesseract
import Utility
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print pytesseract.image_to_string(Image.open('test.jpg'))

image = Utility.screen_grab()
text = Utility.image_text(image)
print text