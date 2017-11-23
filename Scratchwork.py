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



Utility.countdown(5)
enc = Encounter()
enc.update()
power_command = PowerCommand(enc.player_ship.engines, 0)
power_command.execute()
