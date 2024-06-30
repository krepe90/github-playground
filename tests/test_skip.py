import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert True

def test_skip_2():
    if True:
        pytest.skip("no way of currently testing this")
    assert True


@pytest.mark.skipif(1 > 0, reason="1 is greater than 0")
def test_skip_if():
    assert True
