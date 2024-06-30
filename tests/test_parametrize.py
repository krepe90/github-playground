import pytest


def multiply(x: int, y: int) -> int:
    return x * y


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 2),
        (1, 3, 3),
        (2, 3, 6),
        (2, 4, 8),
        (3, 4, 12),
        (3, 5, 15),
        pytest.param(4, 5, 30, marks=pytest.mark.xfail),
        pytest.param(4, 6, 35, marks=pytest.mark.xfail),
    ],
)
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected
