import pytest

from utils import arrs


@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]


@pytest.fixture
def empty_array_fixture():
    return []


def test_get(array_fixture,empty_array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get(empty_array_fixture, 0, "test") == "test"
    assert arrs.get(array_fixture, -2,) == None


def test_slice(array_fixture,empty_array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(empty_array_fixture, 5) == []
    assert arrs.my_slice(array_fixture, -2) == [3, 4]
    assert arrs.my_slice(array_fixture, -9) == [1, 2, 3, 4]


