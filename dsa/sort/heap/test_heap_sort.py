import pytest

from dsa.sort.heap.heap_sort import heap_sort


@pytest.mark.parametrize("input, expected", [
    (
        [5, 2, 3, 1, 4],
        [1, 2, 3, 4, 5],
    ),
    (
        [2, 3, 1, 4, 5],
        [1, 2, 3, 4, 5],
    ),
    (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ),
    (
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ),
    (
        [4, 4, 1, 3, 2, 5, 4],
        [1, 2, 3, 4, 4, 4, 5],
    ),
    (
        [123, 2, 54, 65],
        [2, 54, 65, 123]
    )
])
def test_heap_sort(input, expected):
    heap_sort(input)
    assert input == expected
