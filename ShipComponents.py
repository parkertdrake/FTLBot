"""
This file holds all the classes and subclasses for ship components.
Systems, subsystems, weapons, etc.
"""

"""
System parent class, we can decompose systems like this...
    Every system has a health level
    Every system has a power_level
    capacity power
    
    So any functions to do with health or power can live here.
"""
class System:
    """
    constructor
    @:param capacity: power capacity of the system
    @:param health: current health status of the system (number of intact bars)
    @:param power_level: current power level of the system
    """
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level

    """
    Change power of system to target level. Does bounds checking to ensure you can't overshoot capacity of the system.
    TODO: figure out how to handle bounds checking when the system is not totally healthy
    @:param target_level: desired power level
    """
    def change_power(self, target_level):
        if target_level > self.capacity:
            self.power_level = self.capacity
        else:
            self.power_level = max(target_level, 0)





"""
Class for weapons systems
    weapons systems have weapons (which I will implement separately as they have their own properties)
"""
class WeaponSystem(System):
    def __init__(self):

"""
Class for shield systems
    Shield systems have numbers of shield bubbles (2 power per shield bubble)
"""
class ShieldSystem(System):
    def __init__(self):

"""
Class for engines
    Engine systems have no extra properties
"""
class EngineSystem(System):
    def __init__(self):

"""
Class for MedBays
    No extra properties, maybe healing rate or something?
"""
class MedBaySystem(System):
    def __init__(self):

class OxygenSystem(System):
    def __init__(self):







class Crew()
