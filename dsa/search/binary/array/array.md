# Binary Search (Array)

Binary Search reduces the search area of a sorted array by half on each iteration.

If the value at the midpoint is equal to the value, the midpoint is returned.

If the value at the midpoint is greater than the value, the next iteration only searches in the left half of the array.

If the value at the midpoint is less than the value, the next iteration only searches in the right half of the array.

## Implementation

1. Find midpoint m of array.
2. Set left l and right r indexes.
3. While l is less than or equal to r
4. ----if value of array at index m is equal to value, return m
5. ----if value of array at index m is greater than value, set r to m - 1.
6. ----if value of array at index m is less than value, set l to m + 1.
7. If while loop completes and value is not found, return -1

## Time Complexity

O(logn)

## Space Complexity

O(1) auxillary
