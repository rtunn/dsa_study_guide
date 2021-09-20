import pytest
import random

from dsa.trees.bst.bst import BST, TreeNode


@pytest.fixture
def bst():
    return BST()


def test_insert_sets_root_if_root_is_none(bst):
    bst.insert(5)
    assert bst.root.value == 5


def test_insert_returns_existing_node_if_value_exists(bst):
    expect = bst.insert(5)
    result = bst.insert(5)
    assert id(result) == id(expect)


def test_insert_places_nodes_in_correct_position(bst):
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)

    assert bst.root.value == 2
    assert bst.root.left.value == 1
    assert bst.root.right.value == 3


def test_search_returns_none_if_root_is_none(bst):
    assert bst.search(5) is None


def test_search_returns_none_if_root_is_not_none_but_value_not_present(bst):
    bst.insert(5)
    assert bst.search(6) is None


def test_search_returns_root_if_root_value_matches_search(bst):
    bst.insert(5)
    assert bst.search(5) is bst.root


def test_search_returns_correct_node_in_left_subtree(bst):
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert bst.search(1) is bst.root.left


def test_search_returns_correct_node_in_right_subtree(bst):
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert bst.search(3) is bst.root.right
