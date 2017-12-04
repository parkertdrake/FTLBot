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
import Commands

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
        image = Utility.screen_grab()
        self.enemy_ship = EnemyShip(image)

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
        self.update_player_doors(image)
        self.update_player_weapons(image)

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
        print "updating weapons"
        health, power = self.get_system_health_power(image, Locations.WEAPON_SEGMENTS)
        self.player_ship.weapons.health = health
        self.player_ship.power_level = power
        # determine the power status of the weapons

        artemis = self.player_ship.weapons.artemis
        burst_laser = self.player_ship.weapons.burst_laser

        artemis_locations = Locations.ARTEMIS
        burst_laser_locations = Locations.BURST_LASER

        #artemis check
        for loc in artemis_locations:
            pixel = image[loc[0], loc[1]]
            color = Utility.color(pixel)
            if color == "green" or color == "white":
                artemis.powered = True
                artemis.ready = False
            elif color == "green":
                artemis.ready = True
            else:
                artemis.ready = False
                artemis.powered = False

        #burst laser check
        for loc in burst_laser_locations:
            pixel = image[loc[0], loc[1]]
            color = Utility.color(pixel)
            if color == "green" or color == "white":
                burst_laser.powered = True
                burst_laser.ready = False
            elif color == "green":
                burst_laser.ready = True
            else:
                burst_laser.ready = False
                burst_laser.powered = False


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
            if Utility.color(pixel) == "orange":
                door.is_open = False
            else:
                door.is_open = True


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
        enemy_health = 0
        health_segs = Locations.ENEMY_HULL_SEGMENTS
        for seg in health_segs:
            color = Utility.color(image[seg[0]][seg[1]])
            if color == "green":
                enemy_health += 1
        self.enemy_ship.hull = enemy_health


    """
    Update enemy shield
    @:param image of game screen
    """
    def update_enemy_shield(self, image):
        bubbles = 0
        shield_segs = Locations.ENEMY_BUBBLES
        for seg in shield_segs:
            color = Utility.color(image[seg[0][seg[1]]])
            if color == "blue":
                bubbles += 1
        self.enemy_ship.bubbles = bubbles

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
            if color == "green":
                health += 1
                power += 1
            elif color == "white":
                health += 1
            else:
                break # neither healthy nor powered, we've hit our limit
        return health, power


    """
    Given the current state of the game, generate all valid commands that can be taken.
    """
    def generate_command_set(self):
        # first power commands
        power_commands = []
        # go through engines, shield, medbay, oxygen, and weapons.
        systems = [self.player_ship.engines, \
                   self.player_ship.shields, \
                   self.player_ship.medbay, \
                   self.player_ship.oxygen, \
                   self.player_ship.weapons]
        for system in systems:
            for target_power_level in range(0, system.capacity):
                diff = target_power_level - system.power_level
                if self.player_ship.reactor_available > diff: #you've got enough gas in the tank
                    new_command = Commands.PowerCommand(system, target_power_level)
                    power_commands.append(new_command)



        # then firing commands


        # then venting commands

        pass

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
        print "Shield Bubbles: ", self.enemy_ship.bubbles

    """
    Print the status of both players
    """
    def print_game_status(self):
        self.print_player_status()
        self.print_enemy_status()








