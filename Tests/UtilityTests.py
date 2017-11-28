import unittest
import os
import Utility

"""
Unit tests for utility functions (the ones that make sense anyway)
"""
class TestUtility(unittest.TestCase):
    def test_screen_grab_and_save(self):
        image = Utility.screen_grab(save=True, filename="test.png")
        assert image is not None
        os.remove("test.png")

    def test_color0(self):
        pixel = [0,0,0]
        assert Utility.color(pixel) == "black"

    def test_color1(self):
        pixel = [255,255, 255]
        assert Utility.color(pixel) == "white"

    def test_color2(self):
        pixel = [255, 0, 0]
        assert Utility.color(pixel) == "red"









