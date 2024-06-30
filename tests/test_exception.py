import pytest


def test_exception_1():
    # pass
    with pytest.raises(ZeroDivisionError):
        1 / 0


@pytest.mark.xfail
def test_exception_2():
    # fail
    with pytest.raises(ZeroDivisionError):
        1 / 1


@pytest.mark.xfail
def test_exception_match_regex_1():
    # pass
    with pytest.raises(ValueError, match=r"must be \d+$"):
        raise ValueError("value must be 42")


@pytest.mark.xfail
def test_exception_match_regex_2():
    # fail
    with pytest.raises(ValueError, match=r"must be \d+$"):
        raise ValueError("value must be 42.0")
