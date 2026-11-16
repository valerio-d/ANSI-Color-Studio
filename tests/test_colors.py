# run tests with: PYTHONPATH=src python3 -m unittest discover -s tests
import unittest
from ansicolorstudio.colors import hex_to_rgb, rgb_to_hex, rgb_to_256, colorize

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


class ErrorHandlingTests(unittest.TestCase):
    def test_hex_to_rgb_error(self):
        with self.assertRaises(ValueError):
            hex_to_rgb("######") #expects actual hex code

        with self.assertRaises(TypeError): #missing parameters or parameters incorrect data structure raise TypeError
            hex_to_rgb(123456) #expects string


    def test_rgb_to_hex_error(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(256, 255, -2) #expects values greater than or equal to 0 and lower than or equal to 255
 
        with self.assertRaises(TypeError): #missing parameters or parameters incorrect data structure raise TypeError
            rgb_to_hex("#ffffff") #expects rgb code: int, int , int
            rgb_to_hex((23, 255, 36)) #expects integers not tuple


    def test_rgb_to_256_error(self):
        with self.assertRaises(ValueError):
            rgb_to_256(256, 255, -2)

        with self.assertRaises(TypeError): #missing parameters or parameters incorrect data structure raise TypeError
            rgb_to_256("#ffffff")
            rgb_to_256((23, 255, 36))


    def test_colorize_error(self):
        with self.assertRaises(TypeError):
            colorize("255", 32, 63) #invalid rgb

        with self.assertRaises(ValueError):
            colorize(256, 32, 63) #invalid rgb range

            colorize(255, 32, 63, target="invalid") #invalid target