import pytest

from dsa.sort.bucket.bucket_sort import bucket_sort


@pytest.mark.parametrize("input, expected", [
    (
        [0.5, 0.2, 0.3, 0.1, 0.4],
        [0.1, 0.2, 0.3, 0.4, 0.5],
    ),
    (
        [0.2, 0.3, 0.1, 0.4, 0.5],
        [0.1, 0.2, 0.3, 0.4, 0.5],
    ),
    (
        [0.1, 0.2, 0.3, 0.4, 0.5],
        [0.1, 0.2, 0.3, 0.4, 0.5],
    ),
    (
        [0.5, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.2, 0.3, 0.4, 0.5],
    ),
    (
        [0.4, 0.4, 0.1, 0.3, 0.2, 0.5, 0.4],
        [0.1, 0.2, 0.3, 0.4, 0.4, 0.4, 0.5],
    ),
    (
        [0.65, 0.123, 0.54, 0.2],
        [0.123, 0.2, 0.54, 0.65]
    )
])
def test_bucket_sort(input, expected):
    bucket_sort(input, 10)
    assert input == expected
