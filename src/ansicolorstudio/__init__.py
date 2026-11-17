"""
ANSIColorStudio - an opensource library with mutliple tools for Terminal Text styling and Color Conversion
"""

from .styles import style
from .colors import hex_to_rgb, rgb_to_hex, rgb_to_16, rgb_to_256, colorize
#from .detect import detect

__version__ = "0.1.0"

__all__ = [

    "style", 

    "hex_to_rgb", 

    "rgb_to_hex", 

    "rgb_to_16", 

    "rgb_to_256", 

    "colorize"

    ]