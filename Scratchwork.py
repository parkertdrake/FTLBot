import pytesseract
from GameLibrary import Encounter
import Utility
import numpy as np
from Commands import VentCommand

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


"""
weapons = Utility.load_image_from_file("patches/weapons.png")
shields = Utility.load_image_from_file("patches/shields.png")
engines = Utility.load_image_from_file("patches/engines.png")
helm = Utility.load_image_from_file("patches/helm.png")
oxygen = Utility.load_image_from_file("patches/oxygen.png")

image2 = Utility.load_image_from_file("scanner_checker2.png")

print "scanning"
print "weapons", Utility.scan_for_image(image2, weapons)
print "shields", Utility.scan_for_image(image2, shields)
print "engines", Utility.scan_for_image(image2, engines)
print "helm", Utility.scan_for_image(image2, helm)
print "oxygen", Utility.scan_for_image(image2, oxygen)
"""


# currently confident that enemy image detection works with pf.png
# also works with auto-scout.png
# also works with pirate_scout.png
Utility.countdown(3)
enc = Encounter()


