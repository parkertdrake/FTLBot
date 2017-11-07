"""
Module to hold utility functions for input, screen capture, timing, etc.

"""

import time
import numpy as np
from win32gui import GetForegroundWindow, GetWindowRect
from PIL import ImageGrab
import cv2
import pyautogui

"""
grabs a picture of the window in the foreground. Handles all the positioning and sizing
@:return np array of the screen image
"""
def screen_grab():
    handle = GetForegroundWindow()
    rect = GetWindowRect(handle)
    x = rect[0]
    y = rect[1]
    far_x = rect[2]
    far_y = rect[3]
    return np.array(ImageGrab.grab(bbox=(x, y, far_x, far_y)))

def save_screen(image, filename):
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

"""
counts down from seconds. prints the result
@:param seconds seconds to count down
"""
def countdown(seconds):
    for i in list(range(seconds))[::-1]:
        print(i + 1)
        time.sleep(1)

"""
taps the key specified
@:param key key to be pushed
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
    pyautogui.click(x + col, y + row)


countdown(5)
image = screen_grab()
for i in range(10):
   save_screen(str(i) + ".png")


