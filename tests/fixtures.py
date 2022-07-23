import pytest
from src.robot import Robot


@pytest.fixture
def robot():
    return Robot()
