import pytest
from src.exceptions import InvalidCommand
from src.parser import parse


def test_valid_move():
    line = "MOVE"
    cmd, position = parse(line)

    assert cmd == line
    assert not position


def test_valid_left():
    line = "LEFT"
    cmd, position = parse(line)

    assert cmd == line
    assert not position


def test_valid_right():
    line = "RIGHT"
    cmd, position = parse(line)

    assert cmd == line
    assert not position


def test_valid_report():
    line = "REPORT"
    cmd, position = parse(line)

    assert cmd == line
    assert not position


def test_valid_place():
    expected_pos = dict(x=0, y=0, d="NORTH")
    line = "PLACE 0,0,NORTH"
    cmd, position = parse(line)

    assert cmd == "PLACE"
    assert position == expected_pos


def test_invalid_cmd():
    line = "A"

    with pytest.raises(InvalidCommand):
        cmd, position = parse(line)


def test_place_no_position():
    line = "PLACE"

    with pytest.raises(InvalidCommand):
        cmd, position = parse(line)


def test_place_bad_direction():
    line = "PLACE 0,0,UP"

    with pytest.raises(InvalidCommand):
        cmd, position = parse(line)


def test_place_bad_coords():
    line = "PLACE a,z,NORTH"

    with pytest.raises(InvalidCommand):
        cmd, position = parse(line)
