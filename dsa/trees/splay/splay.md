# Splay Tree

Self-balancing BST that brings most recently searched items to the top of the tree.

## Implementation

The splay tree will need to store nodes, so create a TreeNode data structure that stores the node's value, left child and right child.

### Inserting

If root is null set root to new node.

Splay the new node value. If value exists its node will become root, else root will become the last visited node.

If value of root equals new value, break.

Create new node.

if new value is less than root value, store root's left child as node's left child and store root as new node's right child. Set root's left child to null.

if new value is greater than root value, store root's right child as node's right child and store root as new node's left child. Set root's right child to null.

### Searching

Standard BST search, if node found splay to bring node to root, else splay brings last visited non-null node to root

### Deleting

If root is null, return null.

Splay root with value equal to delete value.

if the root value is not the delete value, return root.

Store references to root's left child and right child, lt and rt.

if lt and rt are both null, set root to null, return root.

If lt is null, set root to rt, return root.

If rt is null, set root to lt, return root.

Splay lt with the value equal to delete value. This finds the largest node in lt and makes it root. Set root's right child to rt. Return root.

### Splaying

There are 7 cases that determine how splaying occurs:

1. node is root -- return root
2. node is left child of root -- rotate right on root
3. node is right child of root -- rotate left on root
4. node is left child of parent p, p is left child of grandparent gp -- rotate right on gp, rotate right on p
5. node is right child of parent p, p is right child of grandparent gp -- rotate left on gp, rotate left on p
6. node is left child of parent p, p is right child of grandparent gp -- rotate right on p, rotate left on gp
7. node is right child of parent p, p is left child of grandparent gp -- rotate left on p,
   rotate right on gp

## Time Complexity

Insert, Search, Delete all have an average running time of O(logn)

## Space Complexity

O(n). Constant space for each node
