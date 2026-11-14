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