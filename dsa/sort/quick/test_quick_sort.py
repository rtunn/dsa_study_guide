import pytest

from dsa.sort.quick.quick_sort import partition, quick_sort


@pytest.mark.parametrize("io", [
    (
        [5, 2, 3, 1, 4],
        3
    )
])
def test_partition(io):
    expect = io[0][-1]
    pivot = partition(io[0], 0, len(io[0]) - 1)
    assert io[0][pivot] == expect


@pytest.mark.parametrize("io", [
    (
        [5, 2, 3, 1, 4]
    ),
    (
        [2, 3, 1, 4, 5]
    ),
    (
        [1, 2, 3, 4, 5]
    ),
    (
        [5, 4, 3, 2, 1]
    )
])
def test_quick_sort(io):
    quick_sort(io, 0, len(io) - 1)
    assert io == [1, 2, 3, 4, 5]
