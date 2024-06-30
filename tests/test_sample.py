import pytest


def add(x: int, y: int) -> int:
    return x + y


def test_add_1():
    assert add(1, 2) == 3


def test_add_2():
    assert add(1, 3) == 4
