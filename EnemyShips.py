"""
Module to hold all enemy ships
Distinguishing between enemy ships basically means seeing where rooms are located.
NOTE: Ship name is not good enough as an identifier. There are multiple "Pirate Scouts" for example.
Also seems that ship layouts are randomized. Big problem.
    Can I scan for features? The icons for systems are a constant.
        Find the location of the icon, and use that to figure out where your targets are.
"""


"""
Super class for enemy ships. Not sure yet if this needs to hold anything really.
"""
class EnemyShip:
    """
    Constructor
    Given image of game screen, figure out where all the targets are, as well as health / shields
    """
    def __init__(self, image):
        # thought, I could create test images that are pictures of the icons.
        # Then start grabbing slices from the enemy region of the screen, think sliding tile.
        # Try to find the locations of the slices that match the icons.
        self.hull = 0
        self.bubbles = 0

        # now we scan for all the major targets - weapons, shields, engines, medbay, helm, etc.
        self.weapons = None
        self.shields = None
        self.engines = None
        self.medbay = None
        self.helm = None



"""
class to hold targets (things to shoot at)
location - row, col pixel location
health - 0 (red), 1(orange), 2(fully functional)
"""
class Target:
    def __init__(self, location):
        self.location = location
        self.health = 2





