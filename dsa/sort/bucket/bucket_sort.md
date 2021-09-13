# Bucket Sort

Stable, non-comparison based sorting algorithm

## bucket_sort

1. Create auxillary array containing slot_count - 1 empty arrays
2. For each value in the input array, calculate the index by taking the integer value of the input value times the slot_count. Append the input value to the array at the calculated index of the auxillary array.
3. Loop from 0 -> slot_count - 1, calling insertion_sort on array at the current index of auxillary array.
4. Set k equal to 0. This will track the index in the input array at which the value will be replaced.
5. Outer loop (i): from 0 -> slot_count - 1
6. Inner loop (j): from 0 -> length of array at index i of auxillary array.
7. Set the value at index k of input array to value of the j index in the i-th array inside the auxillary array
8. Increment k

## Time Complexity

Best: omega(n + k) -- when the list is already sorted
Avg: theta(n + k) -- when the list is uniformly distributed
Worst: O(n^2) -- non-uniformly distributed list
