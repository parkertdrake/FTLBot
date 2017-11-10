"""
A module to hold player ships.
"""

import ShipComponents

"""
Class for the Kestrel, default player ship
"""
class Kestrel:
    def __init__(self):
        self.hull = 30
        self.reactor_available = 0
        self.shields = ShipComponents.ShieldSystem(2, 2, 2) # default Kestrel is fully powered 1 bubble shield
        self.engines = ShipComponents.EngineSystem(2, 2, 2)
        #self.weapons = ShipComponents.WeaponSystem()
        #self.medbay = ShipComponents.MedBaySystem()
        #self.crew = ShipComponents.Crew()

