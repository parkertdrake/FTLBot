"""
Module to hold all enemy ships
Distinguishing between enemy ships basically means seeing where rooms are located.
"""


"""
Super class for enemy ships. Not sure yet if this needs to hold anything really.
"""
class EnemyShip():
    """
    Constructor
    Given name of enemy ship, pulls out the proper parameters from the JSON file
    """
    def __init__(self, name=None):
        # TODO: implement
        # open up the json file, pull the json object for this typ of ship. Name is lookup number.

        #need to track:
        # health,
        # shields,
        # all "targets" -> weapons, shields, o2, engines, medbay
        pass


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



