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
    @:param location: pixel location of the system onscreen. Tuple (row, col). Needed for clicking on the system.
    """
    def __init__(self, capacity, health, power_level, location):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level
        self.location = location

    """
    Change power of system to target level. Does bounds checking to ensure you can't overshoot capacity of the system.
    @:param target_level: desired power level
    """
    def change_power(self, target_level):
        if target_level > min(self.capacity, self.health):
            self.power_level = min(self.capacity, self.health)
        else:
            self.power_level = max(target_level, 0)

"""
Class for weapons systems
    weapons systems have weapons (which I will implement separately as they have their own properties)
    Food for thought - Firing a weapon doesn't have any meaning inside of a weapons system class (fire at what?)
    I'll probably have to pull weapon firing out to the larger Encounter class where it has something to shoot at.
"""
class WeaponSystem(System):
    """
        constructor for weapons system
        @:param capacity: power capacity of the system
        @:param health: current health status of the system (number of intact bars)
        @:param power_level: current power level of the system
        @:param location: pixel location of the system onscreen. Tuple (row, col). Needed for clicking on the system.
        @:param weapons: array of weapons for the weapon system (up to 4)
        """
    def __init__(self, capacity, health, power_level, weapons):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level
        self.weapons = weapons


    """
    Install a new weapon onto the ship.
    """
    def add_weapon(self, weapon):
        if len(self.weapons < 4):
            self.weapons.append(weapon)

    def reorder_weapons(self, weapon_index1, weapon_index2):

        pass

"""
Class for shield systems
    Shield systems have numbers of shield bubbles (2 power per shield bubble)
"""
class ShieldSystem(System):
    """
    constructor for shields
    @:param capacity: power capacity of the system
    @:param health: current health status of the system (number of intact bars)
    @:param power_level: current power level of the system
    @:param bubbles: number of bubbles in the system
    @:param location: pixel location of the system onscreen. Definitely gonna need this for any meaningful targeting system.
    """
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level
        self.bubbles = power_level/2

    """
    Change power of system to target level. Does bounds checking to ensure you can't overshoot capacity of the system.
    Shield bubbles require 2 power to produce each - so an odd power level means you're wasting one power.
    This function ensures you can't change the power level to an odd one. There's no point in half a bubble.
    @:param target_level: desired power level
    """
    def change_power(self, target_level):
        if target_level % 2 == 1:  # bubble check (no wasted power!)
            target_level = target_level - 1
        if target_level > min(self.capacity, self.health):
            self.power_level = min(self.capacity, self.health)
        else:
            self.power_level = max(target_level, 0)

"""
Class for engines
    Engine systems have no extra properties
"""
class EngineSystem(System):
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level
        self.bubbles = power_level/2

"""
Class for MedBays
    No extra properties, maybe healing rate or something?
"""
class MedBaySystem(System):
    """
    constructor
    @:param capacity: power capacity of the system
    @:param health: current health status of the system (number of intact bars)
    @:param power_level: current power level of the system
    @:param location: pixel location of the system onscreen. Tuple (row, col). Needed for clicking on the system.
    """
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level

"""
Class for Oxygen Systems
    No extra properties, maybe oxygenating rate or something?
    Could possibly bundle oxygen level of the whole ship into this
"""
class OxygenSystem(System):
    #TODO: implement oxygen system class
    def __init__(self):
        pass

"""
Class for the crew
Crew is made up of 0 - 6(7? Need to confirm max number of crew) members.
This will be implemented later
"""
class Crew:
    #TODO: implement crew class
    def __init__(self):
        pass

"""
Class to hold crewmembers, later.
"""
class CrewMember:
    # TODO: implement crew member class
    def __init__(self):
        pass

"""
Class to hold rooms on the ship. Might be pretty much just a pixel location. Later.
"""
class RoomSystem:
    #TODO: Implement room class
    def __init__(self):
        pass
