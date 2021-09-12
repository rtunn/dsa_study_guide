import pytest

from dsa.sort.quick3.quick_sort3 import partition3, quick_sort3


@pytest.mark.parametrize("io", [
    (
        [5, 2, 3, 1, 4],
        (3, 3)
    ),
    (
        [4, 4, 1, 3, 2, 5, 4],
        (3, 5)
    )
])
def test_partition(io):
    expect = io[0][-1]
    p1, p2 = partition3(io[0], 0, len(io[0]) - 1)
    assert io[0][p1] == io[0][p2] == expect


@pytest.mark.parametrize("io", [
    (
        [5, 2, 3, 1, 4],
        [1, 2, 3, 4, 5]
    ),
    (
        [2, 3, 1, 4, 5],
        [1, 2, 3, 4, 5]
    ),
    (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ),
    (
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ),
    (
        [4, 4, 1, 3, 2, 5, 4],
        [1, 2, 3, 4, 4, 4, 5]
    )
])
def test_quick_sort(io):
    quick_sort3(io[0], 0, len(io[0]) - 1)
    assert io[0] == io[1]
