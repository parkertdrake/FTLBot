"""
This file holds all the classes and subclasses for ship components.
Systems, subsystems, weapons, etc.
All these classes do is hold information.
"""

from Locations import Locations

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
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level
        self.key = "w"

        self.artemis = Weapon("artemis", 1)
        self.burst_laser = Weapon("burst_laser_2", 0)


"""
Class to hold weapons and their status
charge, name, index in the system, power status, firing status
"""
class Weapon:
    def __init__(self, name, index):
        self.name = name
        self.index = index # starts at 0
        self.powered = False
        self.ready = False

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
        self.key = "a"

"""
Class for engines
    Engine systems have no extra properties
"""
class EngineSystem(System):
    def __init__(self, capacity, health, power_level):
        self.capacity = capacity
        self.health = health
        self.power_level = power_level
        self.key = "s"

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
        self.key = "d"

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
        self.key = "f"

"""
Class to hold graph of rooms on the ship.
Nodes are rooms, edges are doors.
Room may have a system in it, might not.
"""
class RoomSystem:
    """
    constructor - could possibly implement this with a json file encoding the room positions of various ships
    for now its hardcoded for the Kestrel only
    @:param shields: shields system for this instance of the Kestrel
    @:param engines: engines system for this instance of the Kestrel
    @:param medbay: medbay system for this instance of the Kestrel
    @:param oxygen: oxygen system for this instance of the Kestrel
    @:param weapons: weapons system for this instance of the Kestrel
    """
    def __init__(self, shields, engines, medbay, oxygen, weapons):
        self.rooms = [] # easily iterate over rooms
        self.doors = [] # easily iterate over doors

        #going to generate all the rooms first, then the doors, then the matrix. All hardcoded to the Kestrel.
        # first the "Space" room at index 0
        space_room = Room((-1,-1), None, 0)
        self.rooms.append(space_room)
        # The Kestrel has 17 rooms total
        # 5 major system rooms
        major_room_locations = Locations.ROOMS[0:5]

        self.rooms.append(Room(major_room_locations[0], engines, 1))  # engine room constructed
        self.rooms.append(Room(major_room_locations[1], oxygen, 2))   # oxygen room constructed
        self.rooms.append(Room(major_room_locations[2], weapons, 3))  # weapons room constructed
        self.rooms.append(Room(major_room_locations[3], medbay, 4))   # medbay room constructed
        self.rooms.append(Room(major_room_locations[4], shields, 5))  # shields room constructed

        # 12 do not contain major systems.
        non_major_room_locations = Locations.ROOMS[5:]

        for i in range(12):
            self.rooms.append(Room(non_major_room_locations[i], None, i + 6))

        # now we need to do doors.
        # if there are multiple doors between the same two rooms, I'm only going to take the upper left one.
        # using that scheme, there are 22 doors on the Kestrel I care about
        door_locations = Locations.DOORS
        for i in range(22):
            self.doors.append(Door(door_locations[i], False))

        # now we create the adjacency matrix for the graph, initialize 17 x 17 of None
        self.matrix = []
        for i in range(18):
            mat_row = []
            for j in range(18):
                mat_row.append(None)
            self.matrix.append(mat_row)

        # Now need to install all the doors, one at a time.
        # There are 22 doors, so 44 edges are needed (all bidirectional)

        self.matrix[0][6] = self.doors[0]
        self.matrix[6][0] = self.doors[0]
        self.matrix[1][6] = self.doors[1]
        self.matrix[6][1] = self.doors[1]
        self.matrix[1][2] = self.doors[2]
        self.matrix[2][1] = self.doors[2]
        self.matrix[2][7] = self.doors[3]
        self.matrix[7][2] = self.doors[3]
        self.matrix[7][3] = self.doors[4]
        self.matrix[3][7] = self.doors[4]
        self.matrix[1][8] = self.doors[5]
        self.matrix[8][1] = self.doors[5]
        self.matrix[8][9] = self.doors[6]
        self.matrix[9][8] = self.doors[6]
        self.matrix[9][3] = self.doors[7]
        self.matrix[3][9] = self.doors[7]
        self.matrix[3][11] = self.doors[8]
        self.matrix[11][3] = self.doors[8]
        self.matrix[3][12] = self.doors[9]
        self.matrix[12][3] = self.doors[9]
        self.matrix[0][10] = self.doors[10]
        self.matrix[10][0] = self.doors[10]
        self.matrix[10][11] = self.doors[11]
        self.matrix[11][10] = self.doors[11]
        self.matrix[11][5] = self.doors[12]
        self.matrix[5][11] = self.doors[12]
        self.matrix[0][13] = self.doors[13]
        self.matrix[13][0] = self.doors[13]
        self.matrix[12][13] = self.doors[14]
        self.matrix[13][12] = self.doors[14]
        self.matrix[4][12] = self.doors[15]
        self.matrix[12][4] = self.doors[15]
        self.matrix[5][4] = self.doors[16]
        self.matrix[4][5] = self.doors[16]
        self.matrix[5][14] = self.doors[17]
        self.matrix[14][5] = self.doors[17]
        self.matrix[4][15] = self.doors[18]
        self.matrix[15][4] = self.doors[18]
        self.matrix[14][16] = self.doors[19]
        self.matrix[16][14] = self.doors[19]
        self.matrix[15][16] = self.doors[20]
        self.matrix[16][15] = self.doors[20]
        self.matrix[16][17] = self.doors[21]
        self.matrix[17][16] = self.doors[21]

    """
    Given a room, get references to all its neighbors
    """
    def get_neighbors(self, room):
        neighbors = []
        for potential_neigbor in self.rooms:
            if self.matrix[potential_neigbor.index][room.index] is not None:
                neighbors.append(potential_neigbor)
        return neighbors

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
    @:param location of room (row, col)
    @:param system: system attached to the room
    @:param index: index of room (just for the matrix in the system class) 0 will be for the "space room"
    """
    def __init__(self, location, system, index):
        self.location = location
        self.system = system
        self.index = index

"""
Class for doors
just a location and a flag for open/closed
"""
class Door:
    """
    Constructor for rooms
    @:param location : tuple of pixel location of door (row, col)
    @:param open: boolean, true if door is open, false if closed
    """
    def __init__(self, location, is_open):
        self.location = location
        self.is_open = is_open

"""
Class to hold a set of crew members for the players ship
"""
class Crew:
    """
    Constructor
    @:param image of game screen to use
    """
    def __init__(self, image):
        #TODO implement
        # Thoughts -> we can scan the mouse over all the "cells" in the ship,
            # when we hit a crew member, there will be a popup that shows their name and health.
                # Then we use OCR (already set up) to identify them, and go from there

        # routing crew members is pretty straightforward, each one has a hotkey...

        pass

"""
Class for a single crew member
"""
class CrewMember:
    """
    Constructor
    @:param name of crew member
    @:param room they are currently in
    """
    def __init__(self, name, room):
        #TODO implement
        #Thoughts -> does the crew member need anything else? Probably a hotkey
        pass