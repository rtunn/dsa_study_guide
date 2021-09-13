# Counting Sort

Non-comparison based, unstable algorithm. Used to sort elements with a known range. Most efficient when the range is not much greater than the number of elements.

## counting_sort

1. Set count = array of zeroes with length k + 1 where k is the right inclusive bound of the range
2. Loop over input array, incrementing the value in the count array whose index is equal to the value at input array at i
3. Loop from 1 -> k + 1 incrementing the count at index i by the count at i - 1
4. Loop from n -> 0. Set v equal to value of array at index i. Set cv to count at index v. Set ouput at index cv - 1 to v. Decrement the count at index v.
5. Loop from 0 -> n. Set input array at index i to value of output at index i

## Time Complexity

Best: O(n + k)
Avg: O(n + k)
Worst: O(n + k)

T(n) = n + k + n + n = 3n + k

## Space Complexity

O(n + k)
