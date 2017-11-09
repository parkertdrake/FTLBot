"""
Module to holds Commands class and its subclasses
"""


"""
Commands class, what kind of member variables?
What do commands have in common? Not much, might not need a super class 
"""
class Command:




"""
Targeting commands.
Given a weapon system and a target room. Executing the command means firing the weapon at the room.
"""
class FiringCommand(Command):








"""
Given a system (any system), power it to a certain level. Executing the command means routing the power.
"""
class PowerCommand(Command)

"""
Given a crew member and a room, send them to the room.
"""
class CrewCommand(Command)
