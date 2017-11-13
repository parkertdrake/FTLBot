import pytesseract
import Utility
from time import sleep
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print pytesseract.image_to_string(Image.open('test.jpg'))

img = cv2.imread('yellow.jpg',0)

print type(img)
