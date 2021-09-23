# Red-Black Tree

A Red-Black Tree is a kind of self-balancing BST in which each node stores its "color", red or black.

The Red-Black Tree follows these rules:

1. Every node has a color: red or black.
2. All null nodes are black.
3. Red nodes must not have a red child.
4. Each path from a node to a descendant null node must contain the same number of black nodes.

## Best Use Cases

Prefer Red-Black Tree over AVL Tree if insertions and deletions are more frequent than searches.

## Implementation

### Balancing

Balancing is performed by a combination of recoloring and rotation.

We'll use this representation for the logic:

    grandparent

/ \
auncle parent
/ \
 sibling X

### Inserting

1. Insert new node with color red.
2. If parent is black, break.
3. If auncle is red, change both auncle and parent to black. Change grandparent to red, repeat process for grandparent.
4. If auncle is black, there are 4 possible cases handled as outlined below.
5. After applying appropriate case, check if parent and auncle are red. If so, repeat step 3.

#### Left-Left Case

1. Right rotate grandparent.
2. Swap colors of grandparent and parent.

#### Left-Right Case

1. Left rotate parent.
2. Apply Left-Left case.

#### Right-Right Case

1. Left rotate grandparent.
2. Swap colors of grandparent and parent.

#### Right-Left Case

1. Right rotate parent.
2. Apply Right-Right case.
