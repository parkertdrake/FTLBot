import pytesseract
from GameLibrary import Encounter
import Utility
import numpy as np
from time import sleep
import os
from Commands import VentCommand, FiringCommand, PowerCommand

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


"""
weapons = Utility.load_image_from_file("weapons.png")
shields = Utility.load_image_from_file("shields.png")
engines = Utility.load_image_from_file("engines.png")
helm = Utility.load_image_from_file("helm.png")
oxygen = Utility.load_image_from_file("oxygen.png")

image2 = Utility.load_image_from_file("reference.png")


print "scanning"
print Utility.scan_for_image(image2, weapons)
print Utility.scan_for_image(image2, shields)
print Utility.scan_for_image(image2, engines)
print Utility.scan_for_image(image2, helm)
print Utility.scan_for_image(image2, oxygen)
"""

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
        print ("firing!")
        if enc.enemy_ship.bubbles > 0:
            missile_command.execute()
            sleep(.75)
        laser_command.execute()
    else:
        sleep(.5) # just wait it out
    enc.update()




