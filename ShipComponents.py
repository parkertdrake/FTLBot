"""
This file holds all the classes and subclasses for ship components.
Systems, subsystems, weapons, etc.
All these classes do is hold information.
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

    """
    Reposition weapons in the system
    """
    def reorder_weapons(self, weapon_index1, weapon_index2):
        pass

"""
Class to hold weapons and their status
charge, name, index in the system, power status, firing status
"""
class Weapon:
    def __init__(self, name):
        # TODO: add other parameters
        self.name = name

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
Class for engines
    Engine systems have no extra properties
"""
class EngineSystem(System):
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level

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
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level


"""
Class for the crew
Crew is made up of 0 - 6(7? Need to confirm max number of crew) members.
This class may not need to exist. 
"""
class Crew:
    #TODO: implement crew class
    def __init__(self):
        pass

"""
Class to hold crew members.
A crew member is basically a name and a location. 
Eventually I could track how good my crew members are at certain things, but that's later...
"""
class CrewMember:
    # TODO: implement crew member class
    def __init__(self):
        pass

"""
Class to hold graph of rooms on the ship.
Nodes are rooms, edges are doors.
Room may have a system in it, might not.
"""
class RoomSystem:
    #TODO: Implement room class

    """
    constructor - could possibly implement this with a json file encoding the room positions of various ships
    @:param ship_string: identifier for the the ship, all lowercase. See json file at Resources/Ships.json
    """
    def __init__(self, ship_string):
        pass

"""
Class for rooms. 
A room will have a pixel location.
A room may have one or more of the following: 
    A system. 
    One or more crew members. 
    A tear in the hull. (Don't care for now)
    An oxygen level. (Don't care for now)
"""
class Room:
    """
    Constructor for rooms
    @:param row
    """
    def __init__(self, row, col, System):
        pass