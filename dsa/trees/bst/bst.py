from typing import Union


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> TreeNode:
        """Insert a new node if not exists.
        Return either the new node or the node with equal value"""

        if self.root is None:
            self.root = TreeNode(value)
            return self.root
        return self._insert(self.root, value)

    def _insert(self, parent: TreeNode, value: int) -> TreeNode:
        while True:
            if parent.value == value:
                return parent
            if parent.value < value:
                if parent.right is None:
                    parent.right = TreeNode(value)
                    return parent.right
                parent = parent.right
                continue
            if parent.left is None:
                parent.left = TreeNode(value)
                return parent.left
            parent = parent.left

    def search(self, value: int) -> Union[TreeNode, None]:
        """Search for a node with a particular value.
        Return the node if it exists."""

        parent = self.root
        while parent is not None:
            if parent.value == value:
                return parent
            if parent.value < value:
                parent = parent.right
                continue
            parent = parent.left
        return None
