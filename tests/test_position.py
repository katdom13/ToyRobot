import pytest
from src.exceptions import InvalidPosition
from src.position import Position


def test_valid_position():
    data = dict(x=0, y=0, d="NORTH")
    position = Position(data)

    assert position.x == 0
    assert position.y == 0
    assert position.d == "NORTH"


def test_invalid_position():
    data = dict(x=-1, y=-1, d="UP")
    with pytest.raises(InvalidPosition):
        Position(data)
