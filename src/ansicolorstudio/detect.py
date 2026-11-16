# this script decides which colour level to use: none, 16, 256, or truecolor.
import os

validModes = ("auto", "truecolor", "256", "16", "none")

def normalize_mode(mode:str):
    if not isinstance(mode, str):
        raise TypeError("Incorrect data type inputted. Mode must be a string.")

    mode = mode.lower()

    if mode == "rgb":
        mode = "truecolor"

    if mode not in validModes:
        raise ValueError("Mode must be 'auto', 'truecolor', '256', '16', or 'none'.")
    return mode

def detect():
    if "NO_COLOR" in os.environ: #no color (no-color.org)
        return "none"

    if os.environ.get("TERM") == "dumb": #no color
        return "none"

    if os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit"): #check for truecolor - rgb
        return "truecolor"

    if "256color" in os.environ.get("TERM", ""): #check for 256 color
        return "256"

    if os.environ.get("TERM"): #revert to 16
        return "16"

    return "none" #revert to none
