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
    "Black": (0, 0, 0),
    "Red": (128, 0, 0),
    "Green": (0, 128, 0),
    "Yellow": (128, 128, 0),
    "Blue": (0, 0, 128),
    "Magenta": (128, 0, 128),
    "Cyan": (0, 128, 128),
    "White": (192, 192, 192),
    "Bright Black": (128, 128, 128),
    "Bright Red": (255, 0, 0),
    "Bright Green": (0, 255, 0),
    "Bright Yellow": (255, 255, 0),
    "Bright Blue": (0, 0, 255),
    "Bright Magenta": (255, 0, 255),
    "Bright Cyan": (0, 255, 255),
    "Bright White": (255, 255, 255),
}

ESC = '\x1b'
RESET = '\033[0m'

def hex_to_rgb(hexCode: str):
    try: 
        hexCode = hexCode.strip().upper()

        if "#" in hexCode:
            hexCode = hexCode.replace("#", "")

        if len(hexCode) == 6:
            red = int(hexCode[0:2], 16)
            green = int(hexCode[2:4], 16)
            blue = int(hexCode[4:6], 16)

            return (red, green, blue)

        elif len(hexCode) == 3:
            extended = ""
            for letter in hexCode:
                extended += letter + letter

            print(extended)
            return hex_to_rgb(extended)
            
        else:
            raise ValueError('Inputted hex code is incorrect. Please input a valid hex code.')

    except ValueError:
        print('Inputted hex code is incorrect. Please input a valid hex code.')
        return 'Inputted hex code is incorrect. Please input a valid hex code.'


print(hex_to_rgb("#ff8800"))


def rgb_to_hex(red : int, green : int, blue : int):
    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        raise ValueError("Invalid rgb inputted, ensure all values are greater than 0 and not greater than 255")

    return f"#{red:02x}{green:02x}{blue:02x}" #x converts the integer to base 16. 02 keeps the values single-digit.


def rgb_to_256(red : int, green : int, blue : int):
    #check for shades of grey:
    if red == green and green == blue:
        if red < 8:
            return 16 #pure black
        if red > 248:
            return 231 #pure white

        return round(((red - 8) / 247) * 24) + 232 #map the brightness to 24 grey shades (232 to 255)

    #if not grey: sclae each color from 0-255 to 0-5:
    red_small = round((red / 255) * 5)
    green_small = round((green / 255) * 5)
    blue_small = round((blue / 255) * 5)

    #combine the small values using the 6x6x6 color cube formula:
    colorCode = 16 + (36 * red_small) + (6 * green_small) + blue_small
    
    return colorCode


def rgb_to_16(red : int, green : int, blue : int, textOutput = True):
    closestRGB = None
    smallestDistance = float("inf")

    for key, value in ANSI_16_COLORS.items():
        red_16, green_16, blue_16 = value

        distance = ((red - red_16)**2 + (green - green_16)**2 + (blue - blue_16)**2 )**0.5 #eulidean distance

        if distance < smallestDistance: #if the color is closer than the one found save it.
            smallestDistance = distance
            closestRGB = value
            colorName = key

    if textOutput == True:
        return f"closest color: {colorName}, value: {closestRGB}"
    else:
        return {closestRGB}

print(rgb_to_16(255, 10, 10))

def colorize(red : int, green : int, blue : int, mode = "rgb", target="foreground"):
    try:
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ValueError("Invalid rgb inputted, ensure all values are greater than 0 and not greater than 255")

        if target not in ["foreground", "fg", "background", "fg"]:
            raise ValueError("Inputted mode is invalid, please enter either foreground or background.")

        if target in ["background", "bg"]:
            colorType = 48
        else:
            colorType = 38

        return f"{ESC}[{colorType};2;{red};{green};{blue}m"
    
    except ValueError:
        return("ensure that rgb is entered as a tuple and not multiple integers")
