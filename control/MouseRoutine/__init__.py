from control.Routine import Routine


class MouseRoutine(Routine):
    def __init__(self):
        super().__init__()

    def play(self):
        self.play_gen("click", "left")
