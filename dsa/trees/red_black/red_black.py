from enum import Enum, auto
from queue import Queue


class Color(Enum):
    RED = auto()
    BLACK = auto()


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.color = Color.RED
        self.parent = None

    def is_red(self) -> bool:
        return self.color == Color.RED

    def __repr__(self):
        return f'TreeNode(value={self.value}, left={None if self.left is None else self.left.value}' \
            f', right={None if self.right is None else self.right.value}' \
            f', color={"RED" if self.color == Color.RED else "BLACK"}' \
            f', parent={None if self.parent is None else self.parent.value})'


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.ll = False
        self.rr = False
        self.lr = False
        self.rl = False

    def rotate_left(self, node: TreeNode) -> TreeNode:
        x = node.right
        y = x.left
        x.left = node
        node.right = y
        node.parent = x
        if y:
            y.parent = node
        return x

    def rotate_right(self, node: TreeNode) -> TreeNode:
        x = node.left
        y = x.right
        x.right = node
        node.left = y
        node.parent = x
        if y:
            y.parent = node
        return x

    def _insert(self, root: TreeNode, value: int) -> TreeNode:
        conflict = False
        if not root:
            return TreeNode(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
            root.left.parent = root

            if not root is self.root:
                if root.color == Color.RED and root.left.color == Color.RED:
                    conflict = True

        else:
            root.right = self._insert(root.right, value)
            root.right.parent = root

            if not root is self.root:
                if root.color == Color.RED and root.right.color == Color.RED:
                    conflict = True

        if self.ll:
            root = self.rotate_left(root)
            root.color = Color.BLACK
            root.left.color = Color.RED
            self.ll = False

        elif self.rr:
            root = self.rotate_right(root)
            root.color = Color.BLACK
            root.right.color = Color.RED
            self.rr = False

        elif self.rl:
            root.right = self.rotate_right(root.right)
            root.right.parent = root
            root = self.rotate_left(root)
            root.color = Color.BLACK
            root.left.color = Color.RED
            self.rl = False

        elif self.lr:
            root.left = self.rotate_left(root.left)
            root.left.parent = root
            root = self.rotate_right(root)
            root.color = Color.BLACK
            root.left.color = Color.RED
            self.lr = False

        if conflict:
            if root.parent.right is root:
                if root.parent.left is None or root.parent.left.color == Color.BLACK:
                    if root.left and root.left.color == Color.RED:
                        self.rl = True

                    elif root.right and root.right.color == Color.RED:
                        self.ll = True
                else:
                    root.parent.left.color = Color.BLACK
                    root.color = Color.BLACK
                    if not root is self.root:
                        root.parent.color = Color.RED

            else:
                if root.parent.right is None or root.parent.right.color == Color.BLACK:
                    if root.left and root.left.color == Color.RED:
                        self.rr = True

                    elif root.right and root.right.color == Color.RED:
                        self.lr = True

                else:
                    root.parent.right.color = Color.BLACK
                    root.color = Color.BLACK
                    if not root is self.root:
                        root.parent.color = Color.RED
            conflict = False

        return root

    def insert(self, value: int) -> None:
        self.root = self._insert(self.root, value)
        self.root.color = Color.BLACK

    def pre_order(self, node: TreeNode, order: list[TreeNode] = None) -> list[TreeNode]:
        order = [] if order is None else order
        if node is None:
            return order
        order.append(node)
        self.pre_order(node.left, order)
        self.pre_order(node.right, order)
        return order

    def in_order(self, node: TreeNode, order: list[TreeNode] = None) -> list[TreeNode]:
        order = [] if order is None else order
        if node is None:
            return order
        self.in_order(node.left, order)
        order.append(node)
        self.in_order(node.right, order)
        return order

    def post_order(self, node: TreeNode, order: list[TreeNode] = None) -> list[TreeNode]:
        order = [] if order is None else order
        if node is None:
            return order
        self.post_order(node.left, order)
        self.post_order(node.right, order)
        order.append(node)
        return order

    def is_red_compliant(self) -> bool:
        q = Queue(10_000)
        q.put(self.root)
        while not q.empty():
            node = q.get()
            if not node.is_red():
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                continue
            if node.left:
                if node.left.is_red():
                    return False
                q.put(node.left)
            if node.right:
                if node.right.is_red():
                    return False
                q.put(node.right)
        return True
