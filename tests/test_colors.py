# run tests with: PYTHONPATH=src python3 -m unittest discover -s tests
import unittest
from ansicolorstudio.colors import hex_to_rgb, rgb_to_hex, rgb_to_256

class Tests(unittest.TestCase):
    def test_hex_to_rbg(self):
        conversion = hex_to_rgb("#ff0023")
        self.assertEqual(conversion, (255, 0, 35))

    def test_rgb_to_hex(self):
        conversion = rgb_to_hex(40, 50, 71)
        self.assertEqual(conversion, "#283247")

    def test_rgb_to_256(self):
        pure_black = rgb_to_256(6, 6, 6) #should be pure black
        self.assertEqual(pure_black, 16)

        pure_white = rgb_to_256(249, 249, 249) #should be pure white
        self.assertEqual(pure_white, 231)

        gray_shade = rgb_to_256(25, 25, 25)
        expected_gray_shade = int((((25 - 8) / 247) * 24) + 232)
        self.assertEqual(gray_shade, expected_gray_shade)


class ErrorHandlingTests():
    pass