import pytesseract
from GameLibrary import Encounter
import Utility
from Commands import VentCommand

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


Utility.countdown(3)
enc = Encounter()

rooms = enc.player_ship.rooms
engine_room = rooms.rooms[2]
vent_command = VentCommand(engine_room,rooms)
vent_command.execute()

#enc.generate_command_set()



