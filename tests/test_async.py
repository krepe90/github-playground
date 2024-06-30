import asyncio
import pytest
import pytest_asyncio


@pytest_asyncio.fixture
async def list_data():
    await asyncio.sleep(0.1)
    yield [1, 2, 3, 4, 5]
    await asyncio.sleep(0.1)


@pytest.mark.asyncio
async def test_fixture_list_value(list_data: list):
    await asyncio.sleep(0.1)
    assert list_data == [1, 2, 3, 4, 5]
