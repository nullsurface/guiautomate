import argparse
from control.MouseRoutine import MouseRoutine


def record(abspath: bool, path: str):
    routine = MouseRoutine()
    routine.record()

    if abspath:
        routine.save(path)
    else:
        routine.save(f"routines/{path}")


def play(abspath: bool, path: str):
    routine = MouseRoutine()

    if abspath:
        routine.load(path)
    else:
        routine.load(f"routines/{path}")

    routine.play()


mode = {
        "record": record,
        "play": play,
    }


def main(args: argparse.Namespace):
    # If user provided path is absolute or ~
    abspath = args.path[0] == "/" or args.path[0] == "~"

    do = mode.get(args.mode)
    do(abspath, args.path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A GUI Automater Program")

    parser.add_argument("--mode",
                        choices=["record", "play"],
                        help="Record mode records a new routine. Play mode plays back a saved routine.",
                        required=True)
    parser.add_argument("--path",
                        type=str,
                        help="Path of routine to play or record. If not an absolute or ~ path, routines will be stored in routines dir.",
                        required=True)
    main(parser.parse_args())
