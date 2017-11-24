"""
Module to hold the Commands class and its subclasses.
Long term plan, the game library will be able to generate a list of valid commands given a picture of the game state.
It'll serve this list up to whatever agent is making decisions and provide an interface to execute it with.
Design choice -
    Executing a command DOES NOT alter the game state as stored in the encounter. All it does is send keystrokes.
    You execute a single command. After which you must update the game through the encounter.
        I want the encounter to derive its understanding of the game from the image.
        This will prevent drift from what the image of the game is showing vs what it "should" be based on my commands
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
Targeting commands.
Given a weapon system and a target room. Executing the command means firing the weapon at the room.
"""
class FiringCommand(Command):

    """
    Constructor for a firing command
    @:param weapon to do the firing with
    @:param room to target
    """
    def __init__(self, weapon, room):
        self.weapon = weapon
        self.room = room
        self.executed = False

    def execute(self):
        if self.executed:
            return # a command can only be executed once (can I make a function destroy its object?)

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
            pyautogui.press(system.key)
        pyautogui.keyUp("shift")

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

    def execute(self):
        if self.door.is_open == self.target_state:
            return # door is already in the target state
        else:
            Utility.click_screen(self.door.location[0], self.door.location[1])
            self.door.is_open = self.target_state

"""
Given a crew member and a room, send them to the room.
"""
class CrewCommand(Command):
    def __init__(self):
        pass