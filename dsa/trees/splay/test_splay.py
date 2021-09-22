import pytest

from dsa.trees.splay.splay import SplayTree


@pytest.fixture
def splay():
    return SplayTree()


@pytest.fixture
def balanced_splay():
    splay = SplayTree()
    splay.root = splay.get_node(4)
    splay.root.left = splay.get_node(2)
    splay.root.left.left = splay.get_node(1)
    splay.root.left.right = splay.get_node(3)
    splay.root.right = splay.get_node(6)
    splay.root.right.left = splay.get_node(5)
    splay.root.right.right = splay.get_node(7)
    return splay


def test_insert_is_sorted(splay):
    splay.insert(3)
    splay.insert(1)
    splay.insert(4)
    splay.insert(5)
    splay.insert(2)
    assert list(map(lambda node: node.value, splay.in_order(splay.root))) == [
        1, 2, 3, 4, 5]


def test_inserted_node_becomes_root(splay):
    splay.insert(1)
    assert splay.root.value == 1
    splay.insert(2)
    assert splay.root.value == 2


def test_delete_only_item_nullifies_root(splay):
    splay.insert(5)
    splay.delete(5)
    assert splay.root is None


def test_delete_from_left_child(balanced_splay):
    balanced_splay.delete(3)
    assert balanced_splay.root.value == 2


def test_delete_from_right_child(balanced_splay):
    balanced_splay.delete(6)
    assert balanced_splay.root.value == 5


def test_delete_from_left_subtree(balanced_splay):
    balanced_splay.delete(2)
    assert balanced_splay.root.value == 1


def test_delete_from_right_subtree(balanced_splay):
    balanced_splay.delete(5)
    assert balanced_splay.root.value == 4


def test_delete_from_left_subtree_no_left_child_after_splay(balanced_splay):
    balanced_splay.delete(1)
    assert balanced_splay.root.value == 2


def test_delete_from_right_subtree_no_right_child_after_splay(balanced_splay):
    balanced_splay.delete(7)
    assert balanced_splay.root.value == 6


def test_search_returns_none_if_empty(splay):
    assert splay.search(1) is None


def test_search_returns_none_if_value_not_present(splay):
    splay.insert(5)
    assert splay.search(3) is None


def test_search_returns_node_if_value_is_root(splay):
    splay.insert(5)
    assert splay.search(5) is splay.root


def test_search_returns_node_if_value_present_and_not_root(balanced_splay):
    assert balanced_splay.search(7).value == 7


def test_left_case(balanced_splay):
    balanced_splay.rotate_right(balanced_splay.root)
    assert balanced_splay.root.value == 2


def test_right_case(balanced_splay):
    balanced_splay.rotate_left(balanced_splay.root)
    assert balanced_splay.root.value == 6


def test_left_left_case(balanced_splay):
    node = balanced_splay.rotate_right(balanced_splay.root)
    balanced_splay.rotate_right(node)
    assert balanced_splay.root.value == 1


def test_left_right_case(balanced_splay):
    balanced_splay.root.left = balanced_splay.rotate_left(
        balanced_splay.root.left)
    balanced_splay.root = balanced_splay.rotate_right(balanced_splay.root)
    assert balanced_splay.root.value == 3


def test_right_right_case(balanced_splay):
    node = balanced_splay.rotate_left(balanced_splay.root)
    balanced_splay.rotate_left(node)
    assert balanced_splay.root.value == 7


def test_right_left_case(balanced_splay):
    balanced_splay.root.right = balanced_splay.rotate_right(
        balanced_splay.root.right)
    balanced_splay.rotate_left(balanced_splay.root)
    assert balanced_splay.root.value == 5
