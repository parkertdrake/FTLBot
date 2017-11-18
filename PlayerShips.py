"""
A module to hold player ships. For now, just the Kestrel.
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
        self.medbay = ShipComponents.MedBaySystem(1, 1, 1) # 1 power medbay
        self.oxygen = ShipComponents.OxygenSystem(1, 1, 1) # default oxygen system
        #self.weapons = ShipComponents.WeaponSystem()
        #self.crew = ShipComponents.Crew()
        #self.rooms = ShipComponents.RoomSystem()



