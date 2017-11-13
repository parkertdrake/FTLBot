import unittest
import os
import Utility
import GameLibrary

"""
Unit tests for utility functions (the ones that make sense anyway)
"""
class TestLibrary(unittest.TestCase):
    def test_player_hull(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_player_health(img)
        assert enc.player_ship.hull == 29

    def test_player_shield(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_player_shield(img)
        # need to check health, power_level, and bubbles
        assert enc.player_ship.shields.health == 2
        assert enc.player_ship.shields.power_level == 2
        assert enc.player_ship.shields.bubbles == 1

    def test_player_engine(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_player_engine(img)
        assert enc.player_ship.engines.power_level == 1
        assert enc.player_ship.engines.health == 1

    def test_player_medbay(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_player_medbay(img)
        assert enc.player_ship.medbay.power_level == 1
        assert enc.player_ship.medbay.health == 1

    def test_player_oxygen(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_player_oxygen(img)
        assert enc.player_ship.oxygen.power_level == 1
        assert enc.player_ship.oxygen.health == 1

    def test_enemy_hull(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_enemy_health(img)
        assert enc.enemy_ship.hull == 6

    def test_enemy_shields(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update_enemy_shield(img)
        assert enc.enemy_ship.shields == 1

    # all together now
    def test_update(self):
        img = Utility.load_image_from_file("TestInputs/Test.png")
        enc = GameLibrary.Encounter()
        enc.update(img)
        assert enc.enemy_ship.shields == 1
        assert enc.player_ship.hull == 29
        assert enc.enemy_ship.hull == 6



