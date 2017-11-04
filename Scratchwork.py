import numpy as np
from PIL import ImageGrab
import cv2
from win32gui import GetForegroundWindow, GetWindowRect

import time


# this function records a picture of the active window.
# using this I can count on my images of the game always being lined up.


def screen_record():

    i = 0
    while(True):
        # 800x600 windowed mode

        handle = GetForegroundWindow()
        rect = GetWindowRect(handle)
        x = rect[0]
        y = rect[1]
        farx = rect[2]
        fary = rect[3]
        print x, y, farx, fary

        time.sleep(1)
        # starts at 0, 0 (upper left hand corner) and grabs an 800 by 640 image.
        printscreen = np.array(ImageGrab.grab(bbox=(x, y, farx, fary)))
        print printscreen[10, 10]
        #cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        cv2.imwrite('screen_grab' + str(i) + '.png', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))

        i += 1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# gives us time to get situated in the game
for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)

while True:
    screen_record()



