import time
import numpy as np
from win32gui import GetForegroundWindow, GetWindowRect
from PIL import ImageGrab
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

"""
counts down from seconds. prints the result
@:param seconds seconds to count down
"""
def countdown(seconds):
    for i in list(range(seconds))[::-1]:
        print(i + 1)
        time.sleep(1)