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

def rgb_to_hex(rgb:tuple):
    red = int(rgb[0])
    green = int(rgb[1])
    blue = int(rgb[2])

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        raise ValueError("Invalid rgb inputted, ensure all values are greater than 0 and not greater than 255")

    return f"#{red:02x}{green:02x}{blue:02x}" #x converts the integer to base 16. 02 keeps the values single-digit.
    