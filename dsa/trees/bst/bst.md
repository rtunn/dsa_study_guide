# Binary Search Tree

A binary search tree is a tree whose nodes are arranged such that:

-   All values in the left subtree of node are less than the value of the node
-   All values in the right subtree of node are greater than the value of the node
-   Each subtree must be a BST
-   No nodes have duplicate values

## Implementation

The tree will need to store nodes, so create a TreeNode data structure that stores the node's value, left child and right child.

The tree will be initialized with root = None

### Inserting

Start with the root as the parent node.

If the parent is the root node and is null, set the root to the new node

If the parent value is equal to the new value, break.

If the parent value is less than the new value and the parent's right child is not null, the right child becomes the new parent and we start over. If the right child is null, the new node becomes the right child of the parent, break.

If the parent value is greater than the new value and the parent's left child is not null, the left child becomes the new parent and we start over. If the left child is null, the new node becomes the left child of the parent, break.

### Searching

Start with the root as the parent node.

If the parent node is null, return.

If the parent node's value is equal to the search value, return the parent node.

If the parent node's value is less than the search value, the parent node's right child becomes the parent, start over.

If the parent node's value is greater than the search value, the parent node's left child becomes the parent, start over.

## Time Complexity

Inserting and searching both have running time O(h) where h is the height of the tree. In the worst case, a skewed tree, the height may equal the number of nodes n, O(n)

## Space Complexity

O(n) where n is the number of nodes. We must store a constant amount of data for each node.
