import pytesseract
import Utility
from time import sleep
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print pytesseract.image_to_string(Image.open('test.jpg'))

sleep(2)
img = Utility.screen_grab()
Utility.show_screen(img)
sleep(5)
sub_image = img[0:50][0:50]
print "hey"
print Utility.image_text(sub_image)