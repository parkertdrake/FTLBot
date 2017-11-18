"""
Module to holds Commands class and its subclasses.
Long term plan, the game library will be able to generate a list of valid commands given a picture of the game state.
It'll serve this list up to whatever agent is making decisions and provide an interface to execute it with.
"""


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
            return # a command can only be executed once








"""
Given a system (any system), power it to a certain level. Executing the command means routing the power.
"""
class PowerCommand(Command):
    def __init__(self):
        pass

"""
Given a crew member and a room, send them to the room.
"""
class CrewCommand(Command):
    def __init__(self):
        pass