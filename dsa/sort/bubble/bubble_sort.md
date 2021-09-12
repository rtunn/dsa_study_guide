# Bubble Sort

Bubble sort is an unstable comparison sorting algorithm that compares adjacent elements and swaps the elements if A[i] > A[i + 1]

## bubble_sort

1. Loop forever
2. Set inversion count to 0
3. Loop over array from 0 -> n - 2
4. If inversion occurs, swap elements and increment inversion_count
5. After the inner loop completes, break if inversion count == 0

## Time Complexity

Best: O(n) -- Array is already sorted
Avg: O(n^2)
Worst: O(n^2)

## Space Complexity

O(1)
