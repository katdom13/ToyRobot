from re import X, compile

from .exceptions import InvalidCommand


def parse(line):
    line = line.strip()

    PATTERN = compile(
        r"""
            (?<=^)                                    # start
            (?P<cmd>MOVE$|LEFT$|RIGHT$|REPORT$|PLACE  # command
            (?=\s?                                    # space
            (?P<x>\d+),                               # x co-ord
            (?P<y>\d+),                               # y co-ord
            (?P<dir>NORTH|EAST|SOUTH|WEST)            # direction
            $))                                       # EOL
        """,
        X,
    )

    instruction = PATTERN.match(line)
    if not instruction:
        raise InvalidCommand

    cmd = instruction.group("cmd")
    position = None
    if cmd == "PLACE":
        position = dict(x=int(instruction.group("x")), y=int(instruction.group("y")), d=instruction.group("dir"))

    return cmd, position
