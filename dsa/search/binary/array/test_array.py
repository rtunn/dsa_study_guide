from dsa.search.binary.array.array import binary_search
import pytest

from dsa.search.binary.array.array import binary_search


@pytest.fixture
def odd_arr():
    return [1, 2, 3, 4, 5, 6, 7]


@pytest.fixture
def even_arr():
    return [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize("value,index", [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (6, 5),
    (7, 6)
])
def test_returns_correct_index_when_present_in_odd_length_array(odd_arr, value, index):
    assert binary_search(odd_arr, value) == index


@pytest.mark.parametrize("value,index", [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (6, 5)
])
def test_returns_correct_index_when_present_in_even_length_array(even_arr, value, index):
    assert binary_search(even_arr, value) == index


@pytest.mark.parametrize("value", [-1, 0, 8, 9])
def test_returns_negative_one_if_value_not_present(odd_arr, value):
    assert binary_search(odd_arr, value) == -1
