from .exceptions import InvalidCommand
from .parser import parse
from .robot import Robot


def main(file):
    robot = Robot()

    with open(file) as f:
        for line in f:
            try:
                cmd, position = parse(line)
                if cmd == "PLACE":
                    robot.place(position)
                elif cmd == "LEFT" or cmd == "RIGHT":
                    robot.rotate(cmd)
                elif cmd == "REPORT":
                    print(robot.report())
                else:
                    robot.move()
            except InvalidCommand:
                pass
