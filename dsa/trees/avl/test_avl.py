import pytest

from dsa.trees.avl.avl import AVL, get_balance


@pytest.fixture
def avl():
    return AVL()


def test_get_node(avl):
    node = avl.get_node(3)
    assert node.value == 3
    assert node.height == 1
    assert node.left is None
    assert node.right is None


def test_insert_root(avl):
    node = avl.insert(5)
    assert node is avl.root


def test_insert_is_sorted(avl):
    avl.insert(1)
    avl.insert(5)
    avl.insert(3)
    avl.insert(4)
    avl.insert(2)
    assert list(map(lambda x: x.value, avl.in_order(avl.root))) == [
        1, 2, 3, 4, 5]


def test_insert_is_balanced(avl):
    avl.insert(1)
    avl.insert(5)
    avl.insert(3)
    avl.insert(4)
    avl.insert(2)
    nodes = avl.in_order(avl.root)
    for node in nodes:
        assert abs(get_balance(node)) <= 1
