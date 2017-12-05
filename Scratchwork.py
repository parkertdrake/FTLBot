import pytesseract
from GameLibrary import Encounter
import Utility
import Locations
import pyautogui
from time import sleep
from PIL import Image
from Commands import PowerCommand, VentCommand
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


Utility.countdown(3)
enc = Encounter()
rooms = enc.player_ship.rooms
engine_room = rooms.rooms[3]
vent_command = VentCommand(engine_room,rooms)
vent_command.execute()



