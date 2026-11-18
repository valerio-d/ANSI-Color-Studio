import argparse

from .colors import colorize, hex_to_rgb
from .detect import detect, normalize_mode
from .styles import style


def flagsBuilder(args):
    flag_map = {
        "bold": "bold",
        "italic": "italic",
        "dim": "dim",
        "underline": "underline",
        "strike": "strikethrough",
        "reverse": "reverse"
    }

    if isinstance(args, argparse.Namespace):
        values = vars(args)
    else:
        values = args

    flags = []

    for arg_name, flag_name in flag_map.items():
        if values.get(arg_name):
            flags.append(flag_name)

    return flags


def build_parser():
    parser = argparse.ArgumentParser(description = "ANSIColorStudio - terminal text styling and color conversion")
    parser.add_argument("text", nargs = "+", help = "text to style")#nargs = "+" ensures that at least one argument is accepted and returned as a list

    parser.add_argument("--foreground", metavar = "HEX", help = "foreground hex color")
    parser.add_argument("--background", metavar = "HEX", default = None, help = "background hex color")
    
    parser.add_argument("--bold", action = "store_true", help = "apply bold")
    parser.add_argument("--italic", action = "store_true", help = "apply italic")
    parser.add_argument("--dim", action = "store_true", help = "apply dim")
    parser.add_argument("--underline", action = "store_true", help = "apply underline")
    parser.add_argument("--strike", dest = "strike", action = "store_true", help = "apply strikethrough")
    parser.add_argument("--reverse", action = "store_true", help = "apply reverse")

    parser.add_argument("--fg", action = "store_true", help = "apply the color as a foreground instead of background")
    parser.add_argument("--bg", action = "store_true", help = "apply the color as a background instead of a foreground")
    parser.add_argument("--mode", choices = ("auto", "16", "256", "rgb", "truecolor"), default = "auto", help = "select a color mode (default: detect automatically)")

    parser.add_argument("--raw", action = "store_true", default = False, help = "print only the ANSI color sequence")

    return parser

def main():
    parser = build_parser() #build the parser
    args = parser.parse_args() #get the arguments

    text = " ".join(args.text) #join all the words in the list into one single string
    flags = flagsBuilder(args) #get the flags as their actual name rather than a boolean

    
    print(style(text = text, foreground = args.foreground, background = args.background, flags = flags, mode = args.mode, raw = args.raw))

#python -m ansicolorstudio Hello --foreground "#ff8800" --bold