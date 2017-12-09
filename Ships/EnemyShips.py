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
        weapon_image = Utility.load_image_from_file("patches/weapons.png")
        sub_search_image = image[0:1340,1650:]
        print "scanning"

        weapons_loc = Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("patches/weapons.png"))
        shields_loc =  Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("patches/shields.png"))
        engines_loc =  Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("patches/engines.png"))
        oxygen_loc =  Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("patches/oxygen.png"))
        helm_loc =  Utility.scan_for_image(sub_search_image, Utility.load_image_from_file("patches/helm.png"))

        weapons_loc[1] += 1650
        shields_loc[1] += 1650
        engines_loc[1] += 1650
        oxygen_loc[1] += 1650
        helm_loc[1] += 1650

        print weapons_loc, shields_loc, engines_loc, oxygen_loc, helm_loc



"""
class to hold targets (things to shoot at)
location - row, col pixel location
health - 0 (red), 1(orange), 2(fully functional)
"""
class Target:
    def __init__(self, location, health=2):
        self.location = location
        self.health = health




