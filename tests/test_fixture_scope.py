import pytest


@pytest.fixture(scope="function")
def name_list():
    return ["Alice", "Bob", "Charlie"]


@pytest.fixture(scope="class")
def name_list_class():
    return ["Alice", "Bob", "Charlie", "David"]


def test_fixture_scope_1(name_list):
    # pass
    name_list.append("David")
    assert name_list == ["Alice", "Bob", "Charlie", "David"]


def test_fixture_scope_2(name_list):
    # pass
    assert name_list == ["Alice", "Bob", "Charlie"]


class TestFixtureScope:
    def test_fixture_scope_3(self, name_list_class):
        # pass
        name_list_class.append("Eve")
        assert name_list_class == ["Alice", "Bob", "Charlie", "David", "Eve"]

    @pytest.mark.xfail
    def test_fixture_scope_4(self, name_list_class):
        # fail
        # 3번 테스트에서 추가했던 "Eve"가 그대로 남아있다
        assert name_list_class == ["Alice", "Bob", "Charlie", "David"]
