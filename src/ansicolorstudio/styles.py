from .colors import hex_to_rgb, colorize
from .detect import detect, normalize_mode

ESC = '\x1b'
RESET = f'{ESC}[0m'

BOLD = f'{ESC}[1m'
DIM = f'{ESC}[2m'
ITALIC = f'{ESC}[3m'
UNDERLINE = f'{ESC}[4m'
REVERSE = f'{ESC}[7m'
STRIKETHROUGH = f'{ESC}[9m'

def style(text:str, foreground: str = None, background: str = None, flags: tuple | list = None, mode = "auto"):
  mode = normalize_mode(mode)

  if mode == "auto":
    mode = detect()

  if mode == "none":
    return text #return just plain text because even a reset sequence such as \x1b[0m can pollute logs, confuse terminals, violate the expectation that the color-disabled output is safe and transparent, etc.

  return style_builder(text, foreground=foreground, background=background, flags=flags, mode=mode)


def style_builder(text: str, foreground: str = None, background: str = None, flags: tuple | list = None, mode = "truecolor"):
  if mode == "none":
    return text

  if foreground:
    try:
      foreground_rgb = hex_to_rgb(foreground)
      red = int(foreground_rgb[0])
      green = int(foreground_rgb[1])
      blue = int(foreground_rgb[2])
      text = f"{colorize(red, green, blue, mode, target="foreground")}{text}{RESET}"

    except ValueError as e:
      print(e)

  if background:
    try:
      background_rgb = hex_to_rgb(background)
      red = int(background_rgb[0])
      green = int(background_rgb[1])
      blue = int(background_rgb[2])
      text = f"{colorize(red, green, blue, mode, target="background")}{text}{RESET}"

    except ValueError as e:
      print(e)

  try:
    if flags is not None:
      if 'bold' in flags:
        text = f'{BOLD}{text}'

      if 'dim' in flags:
        text = f'{DIM}{text}'

      if 'italic' in flags:
        text = f'{ITALIC}{text}'

      if 'underline' in flags:
        text = f'{UNDERLINE}{text}'

      if 'reverse' in flags:
        text = f'{REVERSE}{text}'

      if 'strikethrough' in flags:
        text = f'{STRIKETHROUGH}{text}'

    return f'{text}{RESET}'

  except TypeError:
    return 'Error: flags must be a tuple or list'


print(style(text='Hello', foreground="#33ff00", flags=('strikethrough', 'underline'), mode="auto"))
