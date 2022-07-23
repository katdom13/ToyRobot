from .constants import DIR_STATE
from .exceptions import InvalidPosition
from .position import Position


class Robot(object):
    position = None

    def place(self, position):
        try:
            self.position = Position(position)
        except InvalidPosition:
            pass

    def move(self):
        if not self.position:
            return

        position = self.position.current()
        try:
            direction = position["d"]
            if direction == "NORTH":
                position["y"] += 1
            elif direction == "SOUTH":
                position["y"] -= 1
            elif direction == "EAST":
                position["x"] += 1
            elif direction == "WEST":
                position["x"] -= 1

            self.position = Position(position)
        except InvalidPosition:
            pass

    def rotate(self, direction):
        if not self.position:
            return

        position = self.position.current()

        try:
            position["d"] = DIR_STATE[position["d"]][direction]
            self.position = Position(position)
        except InvalidPosition:
            pass

    def report(self):
        if not self.position:
            return

        return self.position
