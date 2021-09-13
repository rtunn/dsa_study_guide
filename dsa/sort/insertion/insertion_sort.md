# Insertion Sort

Stable, comparison based sorting algorithm.

## insertion_sort

1. Iterate from 1 -> n
2. Set key equal to value of input array at index i
3. Set j equal to i - 1
4. While j greater than or equal to 0 and key less than or equal to the value of input array at index j
5. Set value of input array at index j + 1 to value of input array at index j
6. Decrement j
7. After while loop completes, set the value of input array at index j + 1 to key

## Time Complexity

Best: omega(n) -- already sorted array
Worst: O(n^2) -- reverse sorted array

## Space Complexity

O(1) Auxillary
