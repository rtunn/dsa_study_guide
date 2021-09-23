def binary_search(arr, x):
    l = 0
    m = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == x:
            return m

        if arr[m] < x:
            l = m + 1
            continue

        if arr[m] > x:
            r = m - 1
            continue

    return -1
