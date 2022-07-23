import os
from pathlib import Path

from src.controller import main

BASE_DIR = Path(__file__).resolve().parent.parent


def test_valid_files(capsys):
    filename = os.path.join(BASE_DIR, "examples", "sample1.txt")

    main(filename)
    out, err = capsys.readouterr()
    assert out == "0,1,NORTH\n"

    filename = os.path.join(BASE_DIR, "examples", "sample2.txt")

    main(filename)
    out, err = capsys.readouterr()
    assert out == "0,0,WEST\n"

    filename = os.path.join(BASE_DIR, "examples", "sample3.txt")

    main(filename)
    out, err = capsys.readouterr()
    assert out == "3,3,NORTH\n"


def test_valid_file_with_invalid_commands(capsys):
    filename = os.path.join(BASE_DIR, "examples", "sample4.txt")

    main(filename)
    out, err = capsys.readouterr()
    assert out == "1,1,EAST\n"


def test_invalid_file(capsys):
    filename = os.path.join(BASE_DIR, "examples", "sample5.txt")

    main(filename)
    out, err = capsys.readouterr()
    assert out == ""
