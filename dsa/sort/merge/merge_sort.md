# Merge Sort

Stable sorting technique using divide and conquer

## merge_sort

1. Check length > 1
2. Find midpoint
3. Recursive call on left array
4. Recursive call on right array
5. Call merge

## merge

1. Create an empty auxillary array
2. While both arrays have untouched indexes, check if the current left index has value greater than current right index's value
3. If so, append right index's value to auxillary array and increment the right index
4. Else, append left index's value to auxillary array and increment left index
5. One of the arrays will have at least one remaining item. Append the remaining items, in order, to the auxillary array
6. In-place replace the slice of the original array with the auxillary array

## Time Complexity

Best: N logN
Avg: N logN
Worst: N logN

T(N) = 2T(N/2) + theta(N)

## Space Complexity

Worst: N
