import pytesseract
from GameLibrary import Encounter
import Utility
import numpy as np
from Commands import VentCommand

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


# informally test image scanning


# I can generate scanning images in this way...
test_full_image = Utility.load_image_from_file("input.png")

scan_image = Utility.get_sub_image(test_full_image, 72, 89, 45, 30)
Utility.save_screen(scan_image, "scan.png")
scan_image2 = Utility.load_image_from_file("scan.png")



location = Utility.scan_for_image(test_full_image, scan_image2)

print location


