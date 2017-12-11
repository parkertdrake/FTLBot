"""
Module to hold all enemy ships
Distinguishing between enemy ships basically means seeing where rooms are located.
NOTE: Ship name is not good enough as an identifier. There are multiple "Pirate Scouts" for example.
Also seems that ship layouts are randomized. Big problem.
    Can I scan for features? The icons for systems are a constant.
        Find the location of the icon, and use that to figure out where your targets are.
"""

import Utility

"""
Super class for enemy ships. Not sure yet if this needs to hold anything really.
"""
class EnemyShip:
    """
    Constructor
    Given image of game screen, figure out where all the targets are, as well as health / shields
    """
    def __init__(self, image):
        self.hull = 0
        self.bubbles = 0

        # now we scan for all the major targets - weapons, shields, engines, medbay, helm, etc.

        sub_search_image = image[0:1340,1650:]
        Utility.tap_key('space') # pause the game while we scan
        print "scanning"

        weapons_loc = Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("weapons.png"))
        shields_loc = Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("shields.png"))
        engines_loc = Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("engines.png"))
        oxygen_loc = Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("oxygen.png"))
        helm_loc = Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("helm.png"))

        weapons_loc[1] += 1650
        shields_loc[1] += 1650
        engines_loc[1] += 1650
        oxygen_loc[1] += 1650
        helm_loc[1] += 1650

        print weapons_loc, shields_loc, engines_loc, oxygen_loc, helm_loc

        # have all the locations, need to generate the targets
        self.weapons = Target(weapons_loc) if weapons_loc[0] != -1 else None
        self.shields = Target(shields_loc) if shields_loc[0] != -1 else None
        self.engines = Target(engines_loc) if engines_loc[0] != -1 else None
        self.oxygen = Target(oxygen_loc) if oxygen_loc[0] != -1 else None
        self.helm = Target(helm_loc) if helm_loc[0] != -1 else None

        Utility.tap_key("space") #unpause the game

"""
class to hold targets (things to shoot at)
location - row, col pixel location
health - 0 (red), 1(orange), 2(fully functional)
"""
class Target:
    def __init__(self, location, health=2):
        self.location = location
        self.health = health





