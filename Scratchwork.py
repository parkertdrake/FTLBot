import pytesseract
from GameLibrary import Encounter
import Utility
import pyautogui
from time import sleep
from PIL import Image
from Commands import PowerCommand
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print pytesseract.image_to_string(Image.open('test.jpg'))



for i in range(22):
    print "self.matrix[x][y] = self.doors[" + str(i) + "]"
    print "self.matrix[y][x] = self.doors[" + str(i) + "]"
