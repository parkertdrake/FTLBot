import pytesseract
from GameLibrary import Encounter
import Utility
from time import sleep
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print pytesseract.image_to_string(Image.open('test.jpg'))



# Utility.load_image_from_file("Tests/TestInputs")

# Demo code
enc = Encounter()
Utility.countdown(5)
enc.update()
enc.print_player_status()
