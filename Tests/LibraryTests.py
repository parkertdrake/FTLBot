import unittest
import os
import Utility
import GameLibrary

"""
Unit tests for utility functions (the ones that make sense anyway)
"""
class TestLibrary(unittest.TestCase):
    def test_player_hull(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update_player_health(img)
        assert enc.player_ship.hull == 27

    def test_player_reactor(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update_reactor(img)
        assert enc.player_ship.reactor_available == 4

    def test_player_shield(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update_player_shield(img)
        # need to check health, power_level, and bubbles
        assert enc.player_ship.shields.health == 2
        assert enc.player_ship.shields.power_level == 2
        assert enc.player_ship.shields.bubbles == 1

    def test_player_engine(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update_player_engine(img)
        assert enc.player_ship.engines.power_level == 1
        assert enc.player_ship.engines.health == 2

    def test_player_medbay(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update_player_medbay(img)
        assert enc.player_ship.medbay.power_level == 0
        assert enc.player_ship.medbay.health == 0

    def test_player_oxygen(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update_player_oxygen(img)
        assert enc.player_ship.oxygen.power_level == 1
        assert enc.player_ship.oxygen.health == 1


    # all together now
    def test_update(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enc.update(img)
        assert enc.player_ship.hull == 27

    # test identifying the enemy ship
    def test_identify_enemy(self):
        img = Utility.load_image_from_file("TestInputs/reference.png")
        enc = GameLibrary.Encounter()
        enemy_string = enc.identify_enemy(img)
        assert (enemy_string == "Class: Rebel Fighter")



