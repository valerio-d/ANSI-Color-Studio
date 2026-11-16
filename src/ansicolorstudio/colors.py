TRUE_COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255)
}

ANSI_16_COLORS = {
    30: (0, 0, 0), #black
    31: (128, 0, 0), #red
    32: (0, 128, 0), #green
    33: (128, 128, 0),#yellow
    34: (0, 0, 128), #blue
    35: (128, 0, 128), #magenta
    36: (0, 128, 128), #cyan
    37: (192, 192, 192), #white
    90: (128, 128, 128), #bright black
    91: (255, 0, 0),#bright red
    92: (0, 255, 0), #bright green
    93: (255, 255, 0), #bright yellow
    94: (0, 0, 255),#bright blue
    95: (255, 0, 255), #bright magenta
    96: (0, 255, 255), #bright cyan
    97: (255, 255, 255),#bright white
}


ESC = '\x1b'
RESET = '\033[0m'


def hex_to_rgb(hexCode: str):
    if not isinstance(hexCode, str):
        raise TypeError("invalid hex code, hex code must be a string.")

    hexCode = hexCode.strip().upper()

    if "#" in hexCode:
        hexCode = hexCode.replace("#", "")

    if len(hexCode) == 6:
        try:
            red = int(hexCode[0:2], 16)
            green = int(hexCode[2:4], 16)
            blue = int(hexCode[4:6], 16)

            return (red, green, blue)
        
        except ValueError:
            pass

    elif len(hexCode) == 3:
        extended = ""
        for letter in hexCode:
            extended += letter + letter

        return hex_to_rgb(extended)
        

    raise ValueError('Inputted hex code is incorrect. Please input a valid hex code.')


def rgb_to_hex(red : int, green : int, blue : int):
    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        raise ValueError("Invalid rgb inputted, ensure all values are greater than 0 and not greater than 255")

    return f"#{red:02x}{green:02x}{blue:02x}" #x converts the integer to base 16. 02 keeps the values single-digit.


def rgb_to_256(red : int, green : int, blue : int):
    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ValueError("Invalid rgb inputted, ensure all values are greater than 0 and not greater than 255")
    
    #check for shades of grey:
    if red == green and green == blue:
        if red < 8:
            return 16 #pure black
        if red > 248:
            return 231 #pure white

        return int(((red - 8) / 247) * 24) + 232 #map the brightness to 24 grey shades (232 to 255)

    #if not grey: sclae each color from 0-255 to 0-5:
    red_small = round((red / 255) * 5)
    green_small = round((green / 255) * 5)
    blue_small = round((blue / 255) * 5)

    #combine the small values using the 6x6x6 color cube formula:
    colorCode = 16 + (36 * red_small) + (6 * green_small) + blue_small
    
    return colorCode


def rgb_to_16(red : int, green : int, blue : int, textOutput = False):
    closestcode = None
    smallestDistance = float("inf")

    for code, value in ANSI_16_COLORS.items():
        red_16, green_16, blue_16 = value

        distance = ((red - red_16)**2 + (green - green_16)**2 + (blue - blue_16)**2 )**0.5 #eulidean distance

        if distance < smallestDistance: #if the color is closer than the one found save it.
            smallestDistance = distance
            closestRGB = value
            colorCode = code

    if textOutput == True:
        return f"closest color code: {colorCode}, value: {closestRGB}"
    else:
        return colorCode


def colorize(red : int, green : int, blue : int, mode = "truecolor", target="foreground"):
    if not (isinstance(red, int) and isinstance(green, int) and isinstance(blue, int)):
        raise TypeError("Incorrect data type inputted. RGB values must be integers.")

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        raise ValueError("Invalid RGB inputted, ensure all values are greater than 0 and not greater than 255")

    if not isinstance(mode, str):
        raise TypeError("Invalid data type inputted. Mode must be a string.")

    if target.lower() not in ["foreground", "fg", "background", "bg"]:
        raise ValueError("Inputted mode is invalid, please enter either foreground or background.")
    
    if target.lower() in ["background", "bg"]:
        colorType = 48
    else:
        colorType = 38

    if mode == "truecolor":
        return f"{ESC}[{colorType};2;{red};{green};{blue}m"

    if mode == "256":
        colorCode = rgb_to_256(red, green, blue)
        return f"{ESC}[{colorType};5;{colorCode}m"

    closestRGB = rgb_to_16(red, green, blue, textOutput=False)
    colorCode = ANSI_16_COLORS[list(ANSI_16_COLORS.values()).index(closestRGB)]

    return f"{ESC}[{colorCode + 10 if colorType == 48 else colorCode}m"
    
