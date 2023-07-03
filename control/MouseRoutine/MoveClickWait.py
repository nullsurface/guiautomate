import time


class MoveClickWait:
    _x: int
    _y: int
    # _wait == None i
    # is either a terminating mcw,
    # or mcw is waiting for "wait time".
    _wait: int
    _time: float

    def __init__(self, x, y, wait):
        self._x = x
        self._y = y
        self._init_time = time.time()
        self._wait = wait

    # Will DO NOTHING if self._wait is != None
    def init_wait(self, wait: int):
        if self._wait is None:
            self._wait = wait

    def get_init_time(self) -> int:
        return self._init_time
