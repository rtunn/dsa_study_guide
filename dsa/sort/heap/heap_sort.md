# Heap Sort

Unstable, in-place, comparison based sorting algorithm based on binary heap. Works by building a Max-Heap, a complete binary tree in which the value of each child is less than its parent's value. It follows that the root has the largest value of all nodes. The sort works by swapping the root (the largest value) with the i-th node (i from n - 1 to 1), then sifting the i-th node down. After each sift operation completes, the root will again be the largest remaining value. The root is swapped to the i-th position in the array, where it will not be swapped again.

## heap_sort

1. Build MaxHeap: i from midpoint -> 0, call heapify(input array, n, i)
2. Sort Heap: i from n - 1 to 1, swap value of input array at index i with value of input array at index 0, then call heapify(input array, i, 0)

## heapify

## Time Complexity

O(nlogn)

## Space Complexity

O(1) auxillary
