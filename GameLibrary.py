"""
@author: Parker Drake
Module to hold code to interact with the game
Idea: Command objects as the interface between the game library and an outside source
    - Game holds a list of "commands" as available orders

"""

import Utility
from PlayerShips import Kestrel


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
    Wrapper function around all game component update calls
    @:param image: image of game screen    
    """
    def update(self, image):
        self.update_player_health(image)
        self.update_player_shield(image)

    """
    Updates the kestrel's health
    @:param image of game 
    """
    def update_player_health(self, image):
        health = 0  # 0 to start, increment with every green segment found
        pixel_row = 125  # y position of the hull health bar

        #column of health segments
        pixel_columns = [37, 57, 87, 110, 137, 152, 182, 199, 224, 256,
                        285, 299, 331, 350, 371, 401, 419, 442, 472, 498,
                        519, 541, 562, 589, 614, 640, 655, 686, 711, 730]
        for col in pixel_columns:
            pixel = image[pixel_row, col]
            # print x, y, pixel

            if pixel[0] > 40 and pixel[1] > 40 and pixel[2] > 40:  # 120, 255, 120 is the color of the health segments
                health += 1

        self.player_ship.hull = health

    """
    updates players shield power level
    @:param image of game screen
    """
    def update_player_shield(self, image):
        # first count the power level
        shield_power = 0
        col = 187
        row = 1376
        for i in range(10): # no way you've got more than 10 power in your shield system
            pixel = image[row,col]
            if pixel[1] > 200: # is it pretty green?
                shield_power += 1
            row -= 25
        self.player_ship.shields.power_level = shield_power # set it directly, we have evidence that it is this power level.
        #now count the bubbles. Do this separately! It might be fully powered, but we don't know if the shields have taken a hit.
        shield_bubbles = 0
        row = 219
        cols = [60, 105, 160, 205] # columns of shield bubble indicators onscreen
        for col in cols:
            pixel = image[row, col]
            if pixel[2]  > 200: # is it pretty blue?
                shield_bubbles += 1
        self.player_ship.shields.bubbles = shield_bubbles

    """
    Updates player engine status
    """
    def update_player_engine(self, image):
        #need to derive health, power status, and capacity (actually don't need to derive this).
        pass



Utility.countdown(5)
game = Encounter()
image = Utility.screen_grab(True, "Test4.png")
game.update(image)
print "Hull: ", game.player_ship.hull
print "Shield Power: ", game.player_ship.shields.power_level
print "Shield Bubbles: ", game.player_ship.shields.bubbles







