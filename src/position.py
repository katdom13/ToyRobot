from .constants import DIRECTIONS
from .exceptions import InvalidPosition


class Position(object):
    x = None
    y = None
    d = None

    def __init__(self, data):
        if 0 <= data["x"] < 5 and 0 <= data["y"] < 5 and data["d"] in DIRECTIONS:
            self.x = data["x"]
            self.y = data["y"]
            self.d = data["d"]
        else:
            raise InvalidPosition

    def current(self):
        return dict(x=self.x, y=self.y, d=self.d)

    def __repr__(self):
        return f"{self.x},{self.y},{self.d}"
