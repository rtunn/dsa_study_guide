# Quick Sort

Unstable sorting algorithm using divide and conquer technique.

Poor worst case time, but generally very fast in practice.

## quick_sort

1. Early return if sequence length is less than 2
2. retrieve pivot by calling partition
3. call quick_sort recursively for sequence left of pivot and right of pivot

## partition

1. Swap the index chosen by your desired strategy with the last index.
2. pivot = value of last index
3. i = lowest index
4. j = Loop from l -> h - 1
5. If value at index j is less than pivot, swap values at i and j, then increment i
6. When loop completes, swap value at i with value of last index
7. return i

## Time Complexity

Best: n log n
T(n) = 2T(n/2) + theta(n)

Avg: n log n
T(n) = T(k) + T(n - k - 1) + theta(n)

Worst: n^2
T(n) = T(0) + T(n - 1) + theta(n)

## Space Complexity

Avg: log n
Worst: n
Constant space is required for each recursion
