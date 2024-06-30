import pytest


@pytest.fixture
def data2():
    d = {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    }
    return d
