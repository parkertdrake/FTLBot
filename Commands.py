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
    def __init__(self, system, power_level):
        self.system = system
        self.power_level = power_level

        #need to figure out which key we need to push, a for shield, etc.

        if type(system) == ShipComponents.ShieldSystem():
            key = "a"
        elif type(system) == ShipComponents.EngineSystem():
            key = "s"
        elif type(system) == ShipComponents.MedBaySystem():
            key = "d"
        elif type(system) == ShipComponents.OxygenSystem():
            key = "f"
        elif type(system) == ShipComponents.WeaponSystem():
            key = "w"

"""
Given a crew member and a room, send them to the room.
"""
class CrewCommand(Command):
    def __init__(self):
        pass