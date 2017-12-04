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
class EnemyShip():
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



"""
Sub class for pirate scouts. Overrides pixel locations for its systems, health, and shields, etc.
"""
class PirateScout(EnemyShip):
    def __init__(self):
        self.hull = 0
        self.shields = 0
        #health stuff
        self.health_row = 250 # This might(should) be same across all enemy ships, need to figure that out.
        starting_col = 1784
        segment_width = 22
        self.health_cols = []
        col = starting_col
        for i in range(10): # this ship does not have 10 health segments, but it won't matter.
            self.health_cols.append(col)
            col += segment_width
        #shield stuff
        self.shield_row = 314 # again, should be the same across ships, need to confirm this
        self.shield_cols = [1810, 1852, 1896] # I'll just hardcode these



