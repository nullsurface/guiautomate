import enum
from pynput import mouse


def Button(enum):
    pass


def MouseButton(Button):
    mouse.Button.left = "left"
    mouse.Button.middle = "middle"
    mouse.Button.right = "right"


def MouseFunction(enum):
    CLICK = "click"
    DOUBLECLICK = "doubleClick"
