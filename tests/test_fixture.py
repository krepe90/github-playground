import pytest


@pytest.fixture
def data():
    d = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return d


@pytest.fixture
def text_file():
    file = open("tests/sample.txt", "r")
    yield file
    file.close()


def test_fixture_1(data):
    assert data["name"] == "John"
    assert data["age"] == 30
    assert data["city"] == "New York"


def test_fixture_2(data):
    data["name"] = "Jane"
    data["age"] = 25

    assert data["name"] == "Jane"
    assert data["age"] == 25
    assert data["city"] == "New York"

def test_fixture_file(text_file):
    assert text_file.read() == "Hello, World!"


def test_fixture_2(data2):
    assert data2["name"] == "Bob"
    assert data2["age"] == 25
    assert data2["city"] == "Los Angeles"
