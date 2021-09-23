import pytest

from dsa.trees.red_black.red_black import Color, RedBlackTree


@pytest.fixture
def rb():
    return RedBlackTree()


def test_insert_to_empty_tree_makes_new_node_root(rb):
    rb.insert(1)
    assert rb.root.value == 1


def test_insert_value_equal_to_root_returns_root(rb):
    root = rb.insert(1)
    new_node = rb.insert(1)
    assert root is new_node


def test_insert_value_less_than_root_inserts_in_left_subtree(rb):
    rb.insert(2)
    rb.insert(1)
    assert rb.root.left.value == 1


def test_insert_value_larger_than_root_inserts_in_right_subtree(rb):
    rb.insert(1)
    rb.insert(2)
    assert rb.root.right.value == 2


def test_insert_stores_all_values(rb):
    for v in [1, 2, 3, 4, 5]:
        rb.insert(v)
    assert list(map(lambda x: x.value, rb.in_order(rb.root))) == [
        1, 2, 3, 4, 5]


def test_insert_has_no_red_conflict(rb):
    for v in [1, 2, 3, 4]:
        rb.insert(v)
    assert rb.is_red_compliant()
