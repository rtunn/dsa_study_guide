# Radix Sort

Unstable, non-comparison based sorting algorithm. Sorts digit by digit from least significant digit to most significant digit. Uses a modified counting sort as a subroutine to perform actualy sorting.

## radix_sort

1. Set max1 = maximum value in input array
2. Set exp = 1
3. While max1 / exp > 0, call counting sort, then set exp to b \* exp

## Time Complexity

O((n+b) \* logb(k)) where b is the base for represting numbers and k is the largest value

## Space Complexity

O(n+k)
