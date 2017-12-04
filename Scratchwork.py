import pytesseract
from GameLibrary import Encounter
import Utility
import Locations
import pyautogui
from time import sleep
from PIL import Image
from Commands import PowerCommand
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


Utility.countdown(3)
enc = Encounter()
enc.update()
print enc.player_ship.weapons.artemis.powered
print enc.player_ship.weapons.burst_laser.powered


