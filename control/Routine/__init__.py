import json
import time
import pyautogui
from typing import List
from pynput import mouse
from control.Movement import Movement


class Routine:
    _routine: List[Movement]

    def __init__(self):
        self._routine = []

    # Takes pyautogui mouse function, and button type
    def play_gen(self, func, button_type: str):
        for mcw in self._routine:
            print(f"Clicking: ({mcw._x}, {mcw._y}), waiting: {mcw._wait}s")
            do = getattr(pyautogui, func)
            do(x=mcw._x, y=mcw._y, button=button_type)
            if mcw._wait is not None:
                time.sleep(mcw._wait)

    def record(self):
        # TODO listen to keyboard too
        with mouse.Listener(on_click=self.record_pos) as listener:
            listener.join()

    def record_pos(self, x, y, button, pressed):
        if pressed:
            if button == mouse.Button.right:
                return False
            pos = pyautogui.position()

            # If not first MCW of routine, update past MCW wait_time
            if self._routine:
                self._routine[-1].init_wait(
                    time.time() - self._routine[-1].get_init_time()
                )
            # TODO dynamic actions
            self._routine.append(Movement(x=pos[0], y=pos[1], button=button, action="click", wait=None))

            print(f"Mouse clicked at ({x}, {y}) with button {button}")

    def load(self, path: str):
        with open(path, "r") as file:
            routine = json.load(file)
        for mcw in routine:
            self._routine.append(
                Movement(
                    x=int(routine[mcw]["x_pos"]),
                    y=int(routine[mcw]["y_pos"]),
                    button=routine[mcw]["button"],
                    action=routine[mcw]["action"],
                    wait=None if routine[mcw]["wait_time"] == 'None'
                    else float(routine[mcw]["wait_time"]),
                )
            )

    def save(self, path: str):
        routine = {}

        for k, v in enumerate(self._routine):
            routine.update(
                {
                    f"{k}": {
                        "x_pos": f"{v._x}",
                        "y_pos": f"{v._y}",
                        "button": f"{v._button}",
                        "action": f"{v._action}",
                        "wait_time": f"{v._wait}",
                    }
                }
            )

        with open(path, "w") as file:
            json.dump(routine, file)
