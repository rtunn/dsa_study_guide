from typing import Union


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

    def __repr__(self):
        return f'TreeNode({self.value=}, {self.height=}, {self.left=}, {self.right=})'


def get_height(node: Union[TreeNode, None]) -> int:
    if not node:
        return 0
    return node.height


def update_height(node: TreeNode) -> None:
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def get_balance(node: TreeNode) -> int:
    return get_height(node.left) - get_height(node.right)


class AVL:
    def __init__(self):
        self.root = None

    def get_node(self, value: int) -> TreeNode:
        return TreeNode(value)

    def insert(self, value: int) -> TreeNode:
        """Insert a node with given value into tree if not exists.
        Return either the existing node with equal value or the new node."""

        if not self.root:
            self.root = self.get_node(value)
            return self.root
        return self._insert(self.root, value)

    def _insert(self, parent: TreeNode, value: int) -> TreeNode:
        if parent is None:
            return self.get_node(value)
        if value < parent.value:
            parent.left = self._insert(parent.left, value)
        else:
            parent.right = self._insert(parent.right, value)

        # update height
        update_height(parent)

        # Check if node is balanced
        balance = get_balance(parent)
        if abs(balance) <= 1:
            return parent

        # Left-Left
        if balance > 1 and parent.left.value > value:
            return self.rotate_right(parent)

        # Left-Right
        if balance > 1 and parent.left.value < value:
            parent.left = self.rotate_left(parent.left)
            return self.rotate_right(parent)

        # Right-Right
        if balance < -1 and parent.right.value < value:
            return self.rotate_left(parent)

        # Right-Left
        parent.right = self.rotate_right(parent.right)
        return self.rotate_left(parent)

    def rotate_left(self, z: TreeNode) -> TreeNode:
        y = z.right
        t2 = y.left

        # IMPORTANT: if z is root, be sure to set root to y
        if self.root is z:
            self.root = y

        # swap
        y.left = z
        z.right = t2

        # update heights
        update_height(z)
        update_height(y)
        return y

    def rotate_right(self, z: TreeNode) -> TreeNode:
        y = z.left
        t2 = y.right

        # IMPORTANT: if z is root, be sure to set root to y
        if self.root is z:
            self.root = y

        # swap
        y.right = z
        z.left = t2

        # update heights
        update_height(z)
        update_height(y)
        return y

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

    def pre_order(self, node: Union[TreeNode, None], order: list[int] = []) -> list[TreeNode]:
        if node is None:
            return order
        order.append(node)
        self.pre_order(node.left, order)
        self.pre_order(node.right, order)
        return order

    def in_order(self, node: Union[TreeNode, None], order: list[int] = []) -> list[TreeNode]:
        if node is None:
            return order
        self.in_order(node.left, order)
        order.append(node)
        self.in_order(node.right, order)
        return order

    def post_order(self, node: Union[TreeNode, None], order: list[int] = []) -> list[TreeNode]:
        if node is None:
            return order
        self.post_order(node.left, order)
        self.post_order(node.right, order)
        order.append(node)
        return order
