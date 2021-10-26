import pytest

from dsa.trees.fenwick.fenwick import Fenwick, num_sequences


@pytest.fixture
def fw():
    return Fenwick(10)


# @pytest.fixture
# def items():
#     return [2, 5, 3, 4, 1]


# @pytest.fixture
# def bound():
#     return 10


@pytest.fixture
def bit():
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    bit = Fenwick(11)
    for i, a in enumerate(arr):
        bit.add(i, a)
    return bit


def test_add_changes_sum_at_initial_index(fw):
    fw.add(0, 5)
    assert fw.arr[1] == 5


def test_add_changes_sum_at_next_indexes(fw):
    fw.add(0, 5)
    assert fw.arr[2] == 5
    assert fw.arr[4] == 5
    assert fw.arr[8] == 5


def test_add_does_not_change_child_indexes(fw):
    fw.add(0, 5)
    assert fw.arr[3] == 0
    assert fw.arr[5] == 0
    assert fw.arr[6] == 0
    assert fw.arr[7] == 0
    assert fw.arr[9] == 0
    assert fw.arr[10] == 0


def test_add_only_changes_next_indexes(fw):
    fw.add(0, 5)
    fw.add(3, 7)
    assert fw.arr[1] == 5
    assert fw.arr[2] == 5
    assert fw.arr[4] == 12
    assert fw.arr[8] == 12


def test_add_correct_at_all_indexes(bit):
    assert bit.arr == [0, 3, 5, -1, 10, 5, 9, -3, 19, 7, 9, 3]


def test_sum_at_parent_indexes(bit):
    assert bit.sum(0) == 3
    assert bit.sum(1) == 5
    assert bit.sum(3) == 10
    assert bit.sum(7) == 19


def test_sum_at_child_indexes(bit):
    assert bit.sum(2) == 4
    assert bit.sum(4) == 15
    assert bit.sum(5) == 19
    assert bit.sum(6) == 16
    assert bit.sum(8) == 26
    assert bit.sum(9) == 28
    assert bit.sum(10) == 31


def test_query_at_parent_indexes_start_parent(bit):
    assert bit.query(1, 3) == 5
    assert bit.query(3, 7) == 9


@pytest.mark.parametrize('items,expected', [
    ([2, 5, 3, 4, 1], (1, 2)),
    ([2, 1, 3], (0, 0)),
    ([1, 2, 3, 4], (4, 0))
])
def test_num_sequences(items, expected):
    assert num_sequences(items, 10) == expected
