def test_robot_init(robot):
    assert robot


def test_report(robot):
    report = robot.report()
    assert not report

    position = dict(x=0, y=0, d="NORTH")
    robot.place(position)
    report = robot.report()

    assert report
    assert str(report) == "0,0,NORTH"


def test_valid_move(robot):
    position = dict(x=0, y=0, d="NORTH")
    robot.place(position)

    robot.move()
    report = robot.report()

    assert report
    assert str(report) == "0,1,NORTH"

    robot.rotate("RIGHT")
    robot.move()
    report = robot.report()
    assert str(report) == "1,1,EAST"

    robot.rotate("RIGHT")
    robot.move()
    report = robot.report()
    assert str(report) == "1,0,SOUTH"

    robot.rotate("RIGHT")
    robot.move()
    report = robot.report()
    assert str(report) == "0,0,WEST"


def test_invalid_move(robot):
    position = dict(x=0, y=0, d="NORTH")
    robot.place(position)
    old_report = robot.report

    robot.rotate("LEFT")
    robot.move()
    new_report = robot.report

    assert old_report == new_report


def test_rotate(robot):
    position = dict(x=0, y=0, d="NORTH")
    robot.place(position)

    robot.rotate("LEFT")
    assert robot.position.d == "WEST"

    robot.rotate("LEFT")
    assert robot.position.d == "SOUTH"

    robot.rotate("LEFT")
    assert robot.position.d == "EAST"

    robot.rotate("RIGHT")
    assert robot.position.d == "SOUTH"

    robot.rotate("RIGHT")
    assert robot.position.d == "WEST"

    robot.rotate("RIGHT")
    assert robot.position.d == "NORTH"


def test_valid_place(robot):
    position = dict(x=0, y=0, d="NORTH")
    robot.place(position)

    assert robot.position


def test_invalid_place(robot):
    position = dict(x=5, y=5, d="NORTHWEST")
    robot.place(position)

    assert not robot.position
