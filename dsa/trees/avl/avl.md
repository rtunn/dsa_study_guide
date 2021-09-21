# AVL Tree

AVL is a self-balancing BST in which the heights of left and right subtrees must not differ by more than 1 for all nodes.

## Implementation

The AVL tree will need to store nodes, so create a TreeNode data structure that stores the node's value, height, left child and right child.

The tree will be initialized with root = None.

### Inserting

Use the standard insert procedure for BST.

Walk back up the subtree updating the height of each node. Check for an unbalanced node, i.e |left child height - right child height| > 1.

Let w be the newly inserted node, z be the unbalanced node, y be the child of z on path from w to z, and x be the child of y on path w to z.

Re-balance the tree by performing the appropriate rotations on subtree rooted at z.

### Rebalancing Cases

There are 4 cases that dictate how rebalancing is performed:

1. y is left child of z, x is left child of y (Left-Left Case)
2. y is left child of z, x is right child of y (Left-Right Case)
3. y is right child of z, x is right child of y (Right-Right Case)
4. y is right child of z, x is left child of y (Right-Left Case)

### Rebalancing Operations

1. For Left-Left Case, perform right rotation on node z
2. For Left-Right Case, perform left rotation on node y, then right rotation on z
3. For Right-Right Case, perform left rotation on node z
4. For Right-Left Case, perform right rotation on node y, then left rotation on z
