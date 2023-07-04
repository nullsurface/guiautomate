import time
from control.Movement.enums import Button, MouseButton


class Movement:
    """
    A Movement is a screen position,
    and action, and a time to wait after the action.
    """
    _x: int
    _y: int
    # when _wait == None i
    # either terminating or uninit
    _wait: int
    _time: float
    _action: int
    _button: Button

    def __init__(self, x, y, button: Button, wait):
        self._x = x
        self._y = y
        self._init_time = time.time()
        self._button = button
        self._wait = wait

    # Will DO NOTHING if self._wait is != None
    def init_wait(self, wait: int):
        if self._wait is None:
            self._wait = wait

    def get_init_time(self) -> int:
        return self._init_time
