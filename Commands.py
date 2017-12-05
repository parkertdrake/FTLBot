"""
Module to hold the Commands class and its subclasses.
Long term plan, the game library will be able to generate a list of valid commands given a picture of the game state.
It'll serve this list up to whatever agent is making decisions and provide an interface to execute it with.
Design choice -
    Executing a command DOES NOT alter the game state as stored in the encounter. All it does is send keystrokes.
    You execute a single command. After which you MUST update the game through the encounter.
        I want the encounter to derive its understanding of the game from the image.
        This will prevent drift from what the image of the game is showing vs what it "should" be based on my commands
    This is going to cause a hit to performance. But 5-10 commands a second is still pretty good, and I can change this later.
"""

import ShipComponents
import pyautogui
import Utility

"""
Commands class, what kind of member variables?
What do commands have in common? Not much, might not need a super class 
"""
class Command:
    def __init__(self):
        pass

"""
Given a system (any system), power it to a certain level. Executing the command means routing the power.
"""
class PowerCommand(Command):
    """
    Constructor
    @:param system: system to work on
    @:param power_level: target power level of system
    """
    def __init__(self, system, target_power_level):
        self.system = system
        self.power_level = target_power_level

    """
    Execute the command.
    """
    def execute(self):
        # need to figure out which key we need to push, a for shield, etc.
        system = self.system
        target_power_level = self.power_level


        current_power = system.power_level
        diff = abs(current_power - target_power_level)
        if current_power > target_power_level:
            print ("Decreasing, holding shift")
            pyautogui.keyDown("shift")

        if system.key == "a": # this is a shield system
            diff = diff / 2 # only operates in entire shield bubbles
        for i in range(diff):
            print system.key
            pyautogui.keyUp("shift")
            pyautogui.press(system.key)

        if system.key == "w": # this is the weapon system, works differently, only operates in whole weapons
            #TODO implement this
            pass

"""
Targeting commands.
Given a weapon system and a target room. Executing the command means firing the weapon at the room.
"""
class FiringCommand(Command):
    """
    Constructor for a firing command
    @:param weapon to do the firing with
    @:param target - room to target on the enemy ship
    """
    def __init__(self, weapon, target):
        self.weapon = weapon
        self.target = target
        self.executed = False

    def execute(self):
        if self.executed:
            return # can only execute once
        weapon_key = str(self.weapon.index + 1)
        Utility.tap_key(weapon_key)
        Utility.click_screen(self.target.location[0], self.target.location[1])

"""
Commands to vent rooms to space
"""
class VentCommand(Command):
    """
    constructor
    @:param room to be vented
    """
    def __init__(self, room, room_system):
        self.room = room
        # need to find the shortest route between this room and space.
        graph_matrix = room_system.matrix
        room_index = room.index

        # route from index to 0 (space node)
        # use dijkstra's algorithm

        dists = len(graph_matrix) * [1000] # functionally infinite
        print dists
        previous = [-1] * len(graph_matrix)
        dists[room_index] = 0 # start here
        visited = [False] * len(graph_matrix)

        while False in visited:
            min_so_far = 10000000
            node = -1  # node we care about
            for i in range(len(previous)):  # finding node with smallest distance
                if dists[i] < min_so_far and visited[i] == False:
                    min_so_far = dists[i]
                    node = i

            # found it!
            visited[node] = True
            neighbors = room_system.get_neighbors(room_system.rooms[node]) # references to neighbors of node
            print "neighbors of node: ", node
            for v in neighbors:
                v_index = v.index
                print v_index
                alt = dists[node] + 1 # all edge weights are 1
                if alt < dists[v_index]:
                    dists[v_index] = alt
                    previous[v_index] = node

        # at this point previous should hold a traceback from space to our source node
        # chase it back to get the doors
        room_1 = 0 # start at space
        room_2 = previous[0]
        self.door_commands = []
        while (room_1 != room.index):
            door = graph_matrix[room_1][room_2]
            self.door_commands.append(DoorCommand(door, True))
            room_1 = room_2
            room_2 = previous[room_2]

    """
    Vent the room to space
    """
    def execute(self):
        for command in self.door_commands:
            command.execute()


"""
Commands to open and close doors
"""
class DoorCommand(Command):
    """
    Constructor
    @:param door to work on
    @:param want_open: true if you want the door open, false if you want it closed
    """
    def __init__(self, door, want_open):
        self.door = door
        self.target_state = want_open

    """
    Open the door
    """
    def execute(self):
        if self.door.is_open == self.target_state:
            return # door is already in the target state
        else:
            Utility.click_screen(self.door.location[0], self.door.location[1])
