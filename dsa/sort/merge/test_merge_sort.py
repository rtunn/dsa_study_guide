import pytest

from dsa.sort.merge.merge_sort import merge_sort


inputs = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [6, 5, 4, 3, 2, 1],
    [1, 6, 2, 5, 3, 4]
]

outputs = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
]


@pytest.mark.parametrize("io", list(zip(inputs, outputs)))
def test_merge_sort(io):
    a = io[0]
    merge_sort(a, 0, len(a) - 1)
    assert a == io[1]
