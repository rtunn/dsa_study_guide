# Selection Sort

Unstable, in-place, comparison based sorting algorithm.

## selection_sort

1. Outer loop (i): from 0 -> n
2. Set min_idx to i
3. Inner loop (j): from i -> n
4. If value of input array at index min_idx is greater than value of input array at index j, set min_idx to j
5. After inner loop completes, swap values at input array index min_idx and index i

## Time Complexity

O(n^2)

## Space Complexity

O(1)
