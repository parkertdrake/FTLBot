# the game library needs to abstract away all of the hairy stuff.
# I want to have a game object that I can query and retrieve all the properties of the game at that time.
# ie weapon_status = Game.weapons_status()



import cv2

import time





class Game:

    # constructor
    def __init__(self):
        self.kestrel_health = 0

    # given image, update teh status of the Kestrel's health
    def update_kestrel_health(self, image):
        health = 0  # 0 to start, increment with every green segment found
        pixel_row = 125  # y position of the hull health bar

        pixel_columns = [37, 57, 87, 110, 137, 152, 182, 199, 224, 256,
                        285, 299, 331, 350, 371, 401, 419, 442, 472, 498,
                        519, 541, 562, 589, 614, 640, 655, 686, 711, 730]
        for col in pixel_columns:
            pixel = image[pixel_row, col]
            # print x, y, pixel

            if pixel[0] > 40 and pixel[1] > 40 and pixel[2] > 40:  # 120, 255, 120 is the color of the health segments
                health += 1

        self.kestrel_health = health

    def fire_missiles(self):

    #increases weapon power to specified level (if that's too high, it just uses all available power)
    def power_up_weapons(self, level):




game = Game()
print game.kestrel_health


count = 0
while count < 200:
    img = Game.screen_grab()
    game.update_kestrel_health(img)
    cv2.imwrite('SCREEN ' + str(count) + '.png', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    print "Kestrel health: ", game.kestrel_health
    time.sleep(.25)
    count += 1


