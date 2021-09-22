from typing import Union


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'TreeNode(value={self.value}, left={None if self.left is None else self.left.value}' \
            f', right={None if self.right is None else self.right.value})'


class SplayTree:
    def __init__(self):
        self.root = None

    def get_node(self, value: int) -> TreeNode:
        return TreeNode(value)

    def insert(self, value: int) -> TreeNode:
        if self.root is None:
            self.root = self.get_node(value)
            return self.root

        self.root = self.splay(self.root, value)
        if self.root.value == value:
            return self.root

        node = self.get_node(value)
        if self.root.value < value:
            root = self.root
            node.right = root.right
            node.left = root
            root.right = None
            self.root = node
            return self.root

        root = self.root
        node.left = root.left
        node.right = root
        root.left = None
        self.root = node
        return self.root

    def search(self, value: int) -> Union[TreeNode, None]:
        self.root = self.splay(self.root, value)
        if self.root and self.root.value == value:
            return self.root
        return None

    def splay(self, node: Union[TreeNode, None], value: int) -> Union[TreeNode, None]:
        if node is None:
            return node

        if node.value == value:
            return node

        if value < node.value:
            if not node.left:
                return node

            # Left-Left
            if value < node.left.value:
                # recursively move target to left left position
                node.left.left = self.splay(node.left.left, value)
                node = self.rotate_right(node)

            # Left-Right
            elif value > node.left.value:
                # recursivley move target to left right position
                node.left.right = self.splay(node.left.right, value)
                if node.left.right:
                    node.left = self.rotate_left(node.left)

            # if the value was found it will be stored in node.left
            if node.left:
                return self.rotate_right(node)
            return node

        if value > node.value:
            if not node.right:
                return node

            # Right-Right
            if value > node.right.value:
                node.right.right = self.splay(node.right.right, value)
                node = self.rotate_left(node)

            # Right-Left
            elif value < node.right.value:
                node.right.left = self.splay(node.right.left, value)
                if node.right.left:
                    node.right = self.rotate_right(node.right)

            # if the value was found it will be stored in node.right
            if node.right:
                return self.rotate_left(node)
            return node

    def delete(self, value: int):
        if self.root is None:
            return None
        self.root = self.splay(self.root, value)

        if self.root.value != value:
            return self.root

        lt = self.root.left
        rt = self.root.right

        if not lt and not rt:
            self.root = None
            return self.root

        if not lt:
            self.root = rt
            return rt

        if not rt:
            self.root = lt
            return lt

        self.root = self.splay(lt, value)
        self.root.right = rt
        return self.root

    def rotate_left(self, node: TreeNode) -> TreeNode:
        p = node.right
        t2 = p.left

        if self.root is node:
            self.root = p

        p.left = node
        node.right = t2
        return p

    def rotate_right(self, node: TreeNode) -> TreeNode:
        p = node.left
        t2 = p.right

        if self.root is node:
            self.root = p

        p.right = node
        node.left = t2
        return p

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
