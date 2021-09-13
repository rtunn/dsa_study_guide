import pytest

from dsa.sort.counting.counting_sort import counting_sort


@pytest.mark.parametrize("io", [
    (
        [5, 2, 3, 1, 4],
        [1, 2, 3, 4, 5],
        5
    ),
    (
        [2, 3, 1, 4, 5],
        [1, 2, 3, 4, 5],
        5
    ),
    (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        5
    ),
    (
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        5
    ),
    (
        [4, 4, 1, 3, 2, 5, 4],
        [1, 2, 3, 4, 4, 4, 5],
        5
    )
])
def test_counting_sort(io):
    counting_sort(io[0], io[2])
    assert io[0] == io[1]


"""
count = [0 0 0 0 0 0]
output = [0 0 0 0 0]

count = [0 0 1 0 1 0]

count = [0 1 2 3 4 5]

output = [0 0 0 4 0]
output = [1 0 0 4 0]
output = [1 0 3 4 0]
output = []

"""
