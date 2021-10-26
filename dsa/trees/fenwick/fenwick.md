# Fenwick Tree a.k.a Binary Indexed Tree

A Fenwick tree is an array-based data structure used to quickly access and update the sum over a range.

## Use Cases

Fenwick trees can be used to find prefix and suffix sums.

Using two Fenwick trees, one can find the number of items less than or greater than a target element on either side of the target element.

### Find the Number of Increasing/Decreasing Sequences Use Case

If the magnitude of all items in a list are bounded, one can determine the number of increasing and/or decreasing sequences in the list. Build one empty Fenwick tree and one fulfilled Fenwick tree from a list. Use the list item's magnitude as the index and 1 as the value.

## Time Complexity

Both updates and queries run in O(log(n)) time. To build a Fenwick Tree from a list of n elements, the total build time is O(n log(n)).

## Space Complexity

O(n) Auxillary space
