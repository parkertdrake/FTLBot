import unittest
import os
import Utility
import GameLibrary

"""
Unit tests for utility functions (the ones that make sense anyway)
"""
class TestLibrary(unittest.TestCase):
    def test_player_hull(self):
        img = Utility.load_image_from_file("TestInputs/test.png")
        enc = GameLibrary.Encounter()
        enc.update_player_health(img)
        assert enc.player_ship.hull == 29


    def test_player_shield(self):
        pass

    def test_player_engine(self):
        pass

    def test_player_medbay(self):
        pass

    def test_player_oxygen(self):
        pass

    def test_enemy_hull(self):
        pass

    def test_enemy_shields(self):
        pass
    # all together now
    def test_update(self):
        pass


