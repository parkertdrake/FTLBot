"""
Module to hold code to interact with the game
"""

import cv2
import time
import Utility
import Kestrel

# a way I could do this is to store none of the information in "Ship" classes or anything like that.
# the only source of truth is the current image of the game state.
# After all, every member variable in the class would just be based on the latest image. So why store it anywhere? Just cut out the middleman.
# Want to know a new property? Implement a new get function. That's it. No extra member variables.
# We can still be clever in the decomposition of how we retrieve that information (like get me the status of the entire weapons system in one function).
# The only thing I can think that might be useful to store permanently are properties that will never change from the beginning of the encounter to the end.
    # Like enemy ship type, total reactor power available, etc.
    # Would be nice not to have to process that kind of info every time I need it.


#what's the end goal here?
    # I want to have a game/encounter object that I(the AI) can query for all the information I need to make decisions.
    # I don't want to have to guess as to the age of the information. I need to be able to count on it being as up to date as possible.
    # I don't want to have to know anything about pixels or where things are on the screen. I want to be able to do things like:
        # game.get_enemy_health(), game.target_enemy_shields(missiles), game.get_weapon_status(missiles)

class Encounter:

    """
    Encounter constructor
    """
    def __init__(self):
        self.player_ship = Kestrel()

    """
    Updates the kestrel's health
    @:param image of game 
    """
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

    """
    updates kestrel's shield level
    @:param image of game screen
    """
    def update_kestrel_shield(self, image):
        shield = 0
        row = 22
        cols = [60, 109, 152, 202]
        for col in cols:
            pixel = image[row, col]
            if pixel[0] == 27 and pixel[1] == 132 and pixel[2] == 155:
                 shield += 1


    """
    Updates the weapon status of the kestrel
    @:param image of the game screen    
    """
    def update_kestrel_weapons_system(self, image):
        weapon_status = []
        row = 1340
        cols = [517, 710]
        for col in cols:
            status = False  # default not ready to fire
            pixel = image[row, col]
            if pixel[0] == 116 and pixel[1] == 255 and pixel[2] == 121:
                status = True
            weapon_status.append(status)
        self.kestrel_weapon_status = weapon_status

    def update_kestrel_shields_system(self):
        print "hello"

    def power_up_weapons(self, level):
        for i in range (level):
            Utility.tap_key("w")






