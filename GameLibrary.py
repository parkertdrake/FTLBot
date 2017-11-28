"""
@author: Parker Drake
Module to hold code to interact with the game
Idea: Command objects as the interface between the game library and an outside source
    - Game holds a list of "commands" as available orders

"""

import Utility
from PlayerShips import Kestrel
from EnemyShips import *
import Locations

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
        self.enemy_ship = PirateScout()

    # Several functions to update status of player's ship
    """
    Wrapper function around all game component update calls
    @:param image: image of game screen    
    """
    def update(self, image=None):
        if image is None:
            image = Utility.screen_grab()
        #player updates
        self.update_reactor(image)
        self.update_player_health(image)
        self.update_player_shield(image)
        self.update_player_engine(image)
        self.update_player_medbay(image)
        self.update_player_oxygen(image)

        # enemy updates
        #self.update_enemy_health(image)
        #self.update_enemy_shield(image)

    """
    Update reactor availability
    @:param image of game screen
    """
    def update_reactor(self, image):
        reactor_segments = Locations.REACTOR_SEGMENTS
        reactor = 0
        for seg in reactor_segments:
            pixel = image[seg[0]][seg[1]]
            if Utility.color(pixel) == "green":
                reactor += 1
            else:
                break
        self.player_ship.reactor_available = reactor

    """
    Updates the kestrel's health
    @:param image of game 
    """
    def update_player_health(self, image):
        health = 0  # 0 to start, increment with every green segment found
        hull_segments = Locations.PLAYER_HULL_SEGMENTS
        for segment in hull_segments:
            pixel = image[segment[0]][segment[1]]
            color = Utility.color(pixel)
            if color == "green" or color == "red" or color == "yellow" or color == "orange":
                health += 1
            else:
                break
        self.player_ship.hull = health

    """
    updates players shield power level, bubbles, and 
    @:param image of game screen
    """
    def update_player_shield(self, image):

        self.player_ship.shields.health, self.player_ship.shields.power_level = \
            self.get_system_health_power(image, Locations.SHIELD_SEGMENTS)
        #now count the bubbles. Do this separately! It might be fully powered, but we don't know if the shields have taken a hit.
        shield_bubbles = 0
        bubble_locations = Locations.PLAYER_BUBBLES
        for bubble in bubble_locations:
            pixel = image[bubble[0]][bubble[1]]
            if Utility.color(pixel) == "blue":
                shield_bubbles += 1
        self.player_ship.shields.bubbles = shield_bubbles

    """
    Updates player engine status
    """
    def update_player_engine(self, image):
        health, power = self.get_system_health_power(image, Locations.ENGINE_SEGMENTS)
        self.player_ship.engines.health = health
        self.player_ship.engines.power_level = power

    """
    Updates the players medbay
    """
    def update_player_medbay(self, image):
        health, power = self.get_system_health_power(image, Locations.MEDBAY_SEGMENTS)
        self.player_ship.medbay.health = health
        self.player_ship.medbay.power_level = power

    """
    Updates the players oxygen system
    """
    def update_player_oxygen(self, image):
        health, power = self.get_system_health_power(image, Locations.OXYGEN_SEGMENTS)
        self.player_ship.oxygen.health = health
        self.player_ship.oxygen.power_level = power

    """
    Update the players weapon system
    @:param image of game screen 
    """
    def update_player_weapons(self, image):
        #TODO implement
        pass

    """
    Scan the doors on the image and update the open flags
    @:param image of game screen
    """
    def update_player_doors(self, image):
        #TODO implement
        doors = self.player_ship.rooms.doors
        for door in doors:
            location = door.location
            pixel = image[location[0]][location[1]]
            # need to check color of open vs closed?


    # Several functions to update status of enemy's ship
    """
    identifies enemy ship type using OCR
    @:param image
    @:returns enemy ship title (string)
    """
    def identify_enemy(self, image):
        # enemy ship title (row, col, width, height)
        # this gives the top right corner, then width going to the left and height going down.

        title_location = Locations.ENEMY_TITLE
        width = title_location[2]
        height = title_location[3]
        top_row, left_col = title_location[0], title_location[1] - width
        bottom_row, right_col = top_row + height, left_col + width

        sub_image = image[top_row:bottom_row, left_col:right_col]
        text = Utility.image_text(sub_image)
        return text

    """
    Update enemy shield
    @:param image of game screen
    """
    def update_enemy_health(self, image):
        health_cols = self.enemy_ship.health_cols
        seg_width = 22 # width of health segments
        health_row = self.enemy_ship.health_row
        health = 0
        for col in health_cols:
            pixel = image[health_row, col]
            if Utility.color(pixel) == "green":
                health += 1
            else:
                break # if this one's not green, the rest won't be either
            col += seg_width # next health segment
        self.enemy_ship.hull = health

    """
    Update enemy shield
    @:param image of game screen
    """
    def update_enemy_shield(self, image):
        shield_row = self.enemy_ship.shield_row
        shield_cols = self.enemy_ship.shield_cols
        shield_level = 0
        for col in shield_cols:
            pixel = image[shield_row, col]
            if Utility.color(pixel) == "blue":
                shield_level += 1
            else:
                break # if this one's not blue the rest won't be either
        self.enemy_ship.shields = shield_level

    # Some helper functions
    """
    Given image, counts the healthy power segments (powered or unpowered of a system), and the power level 
    This is its own function so I'm not repeating the same for loop for every system
    @:param image: image of the game screen
    @:param segments: pixel locations of the system we're analyzing
    @:returns tuple representing the (health, power) of a system. 
    """
    def get_system_health_power(self, image, segments):
        health = 0
        power = 0
        for segment in segments:
            #analyze the segment by looking at all 10 of the sample pixels in it
            average_pixel = [0, 0, 0]
            for i in range(10):
                pixel = image[segment[i]] # grab the sample pixel
                average_pixel[0] += pixel[0]
                average_pixel[1] += pixel[1]
                average_pixel[2] += pixel[2]
            average_pixel = [x / 10 for x in average_pixel]
            # now look at the color of the average pixel
            color = Utility.color(average_pixel)
            if (color == "green"):
                health += 1
                power += 1
            elif (color == "white"):
                health += 1
            else:
                break # neither healthy nor powered, we've hit our limit
        return health, power


    """
    Get a nice printout of the player's ship status
    """
    def print_player_status(self):
        print "Player Ship Status: "
        print "Hull: ", self.player_ship.hull, "Reactor: ", self.player_ship.reactor_available
        print "Shield Power: ", self.player_ship.shields.power_level, ", Shield Health: ", self.player_ship.shields.health, \
            ", Shield Bubbles: ", self.player_ship.shields.bubbles
        print  "Engine Power: ", self.player_ship.engines.power_level, ", Engine Health: ", self.player_ship.engines.health
        print  "Medbay Power: ", self.player_ship.medbay.power_level, ", Medbay Health: ", self.player_ship.medbay.health
        print  "Oxygen Power: ", self.player_ship.oxygen.power_level, ", Oxygen Health: ", self.player_ship.oxygen.health

    """
    Get a nice printout of the enemy's ship status
    """
    def print_enemy_status(self):
        print "Enemy Ship Status: "
        print "Hull: ", self.enemy_ship.hull
        print "Shield Level: ", self.enemy_ship.shields

    """
    Print the status of both players
    """
    def print_game_status(self):
        self.print_player_status()
        self.print_enemy_status()








