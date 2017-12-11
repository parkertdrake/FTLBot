import pytesseract
from GameLibrary import Encounter
import Utility
import numpy as np
from time import sleep
import os
from Commands import VentCommand, FiringCommand, PowerCommand

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


"""
weapons = Utility.load_image_from_file("patches/weapons.png")
shields = Utility.load_image_from_file("patches/shields.png")
engines = Utility.load_image_from_file("patches/engines.png")
helm = Utility.load_image_from_file("patches/helm.png")
oxygen = Utility.load_image_from_file("patches/oxygen.png")

image2 = Utility.load_image_from_file("scanner_checker2.png")

image_set = [weapons, shields, engines, helm, oxygen]
print "scanning"
print "found images", Utility.scan_for_image(image2, image_set)


# currently confident that enemy image detection works with pf.png
# also works with auto-scout.png
# also works with pirate_scout.png


Utility.countdown(3)
enc = Encounter()
powercommand = PowerCommand(enc.player_ship.weapons, 3)
powercommand.execute()
missiles = enc.player_ship.weapons.artemis
laser = enc.player_ship.weapons.burst_laser
while True:
    if missiles.ready and laser.ready:
        missile_command = FiringCommand(missiles, enc.enemy_ship.shields)
        laser_command = FiringCommand(laser, enc.enemy_ship.weapons)
        print "firing!"
        missile_command.execute()
        laser_command.execute()
    else:
        sleep(.5) # just wait it out
    enc.update()

"""

PATH = "C:/Users/parke/PycharmProjects/FTLBot"
img = None
for path, dirs, files in os.walk(PATH):
    for filename in files:
        if filename == "weapons.png":
            fullpath = os.path.join(path, filename)
            img = open(fullpath)

print type(img)



