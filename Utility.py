"""
Module to hold utility functions for input, screen capture, timing, etc.
If you're thinking of a function that doesn't seem to fit anywhere else, it's here.
"""

import time
import numpy as np
from win32gui import GetForegroundWindow, GetWindowRect
from PIL import ImageGrab
import cv2
import pyautogui
import pytesseract
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract' # needed for tesseract OCR


"""
grabs a picture of the window in the foreground. Handles all the positioning and sizing
@:return np array of the screen image
"""
def screen_grab(save=False, filename="None"):
    handle = GetForegroundWindow()
    rect = GetWindowRect(handle)
    x = rect[0]
    y = rect[1]
    far_x = rect[2]
    far_y = rect[3]
    image = np.array(ImageGrab.grab(bbox=(x, y, far_x, far_y)))
    if (save):
        save_screen(image, filename)
    return image

"""
Helper function for saving images
@:param image: image to save
@:param filename: name desired for file
"""
def save_screen(image, filename):
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

"""
Shows np image onscreen
"""
def show_screen(image):
    cv2.imshow('window',cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

"""
Given image, get the text out of it as a string using tesseract OCR
@:param image: image to be analyzed (as a np array)
@:return string of the text in the image
"""
def image_text(image):
    save_screen(image, 'temp.png') #drop it into a temp file
    text = pytesseract.image_to_string(Image.open('temp.png'))
    os.remove('temp.png')
    return text

"""
Given an image, scan for the location of the subimage
@:param image as np array
@:param subimage to search for, as numpy array
@:return (row, col) tuple of the center of the subimage
"""
def scan_for_image(image, search_image):
    location = (-1, -1)
    im_height = image.shape[0]
    im_width = image.shape[1]
    sub_height = search_image.shape[0]
    sub_width = search_image.shape[1]
    for row in range(im_height):
        for col in range(im_width):
            test_image = get_sub_image(image, row, col, sub_width, sub_height)
            if np.array_equal(test_image, search_image):
                return ((row + sub_height)/2, (col + sub_width)/2)

    return location # no match found

"""
Given an image, grab a subimage. Does do error checking
@:param image to grab slice of
@:param row - physically highest row (lower number = higher row)
@:param col - leftmost col of image (lower number = more to the left)
@:param width of subimage
@:param heigh of subimage
@:return np array of subimage
"""
def get_sub_image(image, row, col, width, height):
    im_height = image.shape[0]
    im_width = image.shape[1]
    sub_image = image[max(0, row):min(im_height, row + height), max(0, col):min(im_width, col + width)]
    return sub_image

"""
counts down from seconds. prints the result
@:param seconds seconds to count down
"""
def countdown(seconds):
    for i in list(range(seconds))[::-1]:
        print(i + 1)
        time.sleep(1)

# some input utility functions
"""
taps the key specified
@:param key key to be pushed as string 
"""
def tap_key(key):
    pyautogui.press(key)

"""
Clicks game screen at specified location
@:param row of click
@:param col of click
"""
def click_screen(row, col):
    handle = GetForegroundWindow()
    rect = GetWindowRect(handle)
    x = rect[0]
    y = rect[1]
    offset = 20 # clicking is off by just a touch
    pyautogui.moveTo(x + col, y + row + offset)
    time.sleep(.01)
    pyautogui.click(x + col, y + row + offset)

"""
Gauges the color of the pixel
@:param pixel: tiny array showing the color of the pixel
@returns: a lowercase string representing the color
"""
def color(pixel):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])

    # pretty tight variance on the colors, and overall high pixel values
    if abs(r - g) < 30 and abs(r - b) < 30 and abs(g - b) < 30 and r + g + b > 715:
        return "white"

    # pretty tight variance on the colors, and overall low pixel values
    if abs(r - g) < 3 and abs(r - b) < 3 and abs(g - b) < 3 and r + g + b < 90:
        return "black"

    # pretty tight variance on the colors, and overall low pixel values
    if abs(r - g) < 15 and abs(r - b) < 15 and abs(g - b) < 15:
        return "gray"

    # high red compared to other values
    if r > g * 2 and r > b * 2 and r > 150:
        return "red"

    # high green compared to other values
    if g > r * 1.5 and g > b * 1.5 and g > 150:
        return "green"

    # high blue compared to other values
    if b > r * 1.5 and b > g * 1.5 and b > 150:
        return "blue"

    if r > 130 and g > 90 and b < 100:
        return "orange"

"""
Given a filename, load an image (primarily using this for testing purposes)
@:param filename of image to load (include the extension)
@:returns np array of the image
"""
def load_image_from_file(filename):
    img = cv2.imread(filename)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2 default color is brg (for some ungodly reason)








