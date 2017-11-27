import pytesseract
from GameLibrary import Encounter
import Utility
import pyautogui
from time import sleep
from PIL import Image
from Commands import PowerCommand
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


Utility.countdown(5)
enc = Encounter()
image = Utility.screen_grab()
enc.update(image)
enc.identify_enemy(image)
enc.print_player_status()


