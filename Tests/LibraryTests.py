import unittest
import os
import Utility
import GameLibrary

"""
Unit tests for utility functions (the ones that make sense anyway)
"""
class TestLibrary(unittest.TestCase):
    def test_player_hull(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(pause=False)
        enc.update_player_health(img)
        assert enc.player_ship.hull == 27

    def test_player_reactor(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_reactor(img)
        assert enc.player_ship.reactor_available == 4

    def test_player_shield(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_player_shield(img)
        # need to check health, power_level, and bubbles
        assert enc.player_ship.shields.health == 2
        assert enc.player_ship.shields.power_level == 2
        assert enc.player_ship.shields.bubbles == 1

    def test_player_engine(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_player_engine(img)
        assert enc.player_ship.engines.power_level == 1
        assert enc.player_ship.engines.health == 2

    def test_player_medbay(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_player_medbay(img)
        assert enc.player_ship.medbay.power_level == 0
        assert enc.player_ship.medbay.health == 0

    def test_player_oxygen(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_player_oxygen(img)
        assert enc.player_ship.oxygen.power_level == 1
        assert enc.player_ship.oxygen.health == 1

    def test_player_weapons(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_player_weapons(img)
        assert enc.player_ship.weapons.artemis.ready == False
        assert enc.player_ship.weapons.burst_laser.ready == False

    def test_player_doors(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_player_doors(img)
        assert enc.player_ship.rooms.doors[1].is_open == False

    # all together now
    def test_update(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update(img)
        assert enc.player_ship.hull == 27

    # testing enemy stuff
    def test_identify_enemy(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enemy_string = enc.identify_enemy(img)
        assert (enemy_string == "Class: Rebel Fighter")

    def test_enemy_hull(self):
        img = Utility.load_image_from_file("eference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_enemy_health(img)
        assert enc.enemy_ship.hull == 9

    def test_enemy_shield(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update_enemy_shield(img)
        assert enc.enemy_ship.bubbles == 1

    #this doesn't actually test a library function, it tests a utility function
    def test_enemy_scan(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(image=img, pause=False)
        enc.update(img)
        weapons_loc = enc.enemy_ship.weapons.location
        shields_loc = enc.enemy_ship.shields.location
        engines_loc = enc.enemy_ship.engines.location
        oxygen_loc = enc.enemy_ship.oxygen.location
        helm_loc = enc.enemy_ship.helm.location

        print weapons_loc
        print shields_loc

        assert weapons_loc[0] == 703
        assert weapons_loc[1] == 2057

        assert shields_loc[0] == 706
        assert shields_loc[1] == 2263

        assert engines_loc[0] == 703
        assert engines_loc[1] == 2161

        assert helm_loc[0] == 344
        assert helm_loc[1] == 2160

        assert oxygen_loc[0] == 559
        assert oxygen_loc[1] == 2230

    def test_enemy_systems(self):
        img = Utility.load_image_from_file("reference.png")
        enc = GameLibrary.Encounter(pause=False)
        enc.update(img)
        assert enc.enemy_ship.weapons.health == 2

