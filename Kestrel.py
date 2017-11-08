"""
A class to hold the Kestrel Ship. Definitely this will need to be extended in the long term for multiple player ships, but we'll start here.


"""


import ShipComponents

class Kestrel:
    def __init__(self):
        self.hull = 30
        self.reactor_available = 0
        self.shields = ShipComponents.ShieldSystem()
        self.weapons = ShipComponents.WeaponSystem()
        self.engines = ShipComponents.EngineSystem()
        self.medbay = ShipComponents.MedBaySystem()
        self.crew = ShipComponents.Crew()

