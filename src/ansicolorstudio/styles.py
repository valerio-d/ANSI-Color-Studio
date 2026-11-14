ESC = '\x1b'
RESET = f'{ESC}[0m'

BOLD = f'{ESC}[1m'
DIM = f'{ESC}[2m'
ITALIC = f'{ESC}[3m'
UNDERLINE = f'{ESC}[4m'
REVERSE = f'{ESC}[7m'
STRIKETHROUGH = f'{ESC}[9m'


def style_builder(text: str, foreground: str = None, background: str = None, flags: tuple = None):
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


print(style_builder('Hello', None, None, flags=('underline', 'dim')))
print(style_builder('Normal text'))
