import pytest

from dsa.sort.bubble.bubble_sort import bubble_sort


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
def test_bubble_sort(io):
    bubble_sort(io[0])
    assert io[0] == io[1]
