import pytest
import random

from dsa.trees.trie.trie import Trie, TrieNode


@pytest.fixture
def trie():
    return Trie()


@pytest.fixture
def foo_trie(trie):
    trie.insert('foo')
    return trie


@pytest.fixture
def saved_words():
    return [
        'foo',
        'food',
        'fool',
        'foods',
        'fools',
        'cats',
        'birds',
        'mice'
    ]


@pytest.fixture
def repo(trie, saved_words):
    for word in saved_words:
        trie.insert(word)
    return trie


def test_get_node_creates_an_empty_node(trie):
    result = trie.get_node()
    assert result.children == [None] * 26
    assert result.is_end_of_word == False


def test_get_node_returns_unique_node(trie):
    assert trie.get_node() != trie.get_node()


def test_insert_adds_new_char_as_child_node(trie):
    trie.insert('a')
    assert isinstance(trie.root.children[0], TrieNode)


def test_insert_marks_end_of_word_on_last_char_only(trie):
    trie.insert('abc')
    a = trie.root.children[0]
    assert a.is_end_of_word is False
    b = a.children[1]
    assert b.is_end_of_word is False
    c = b.children[2]
    assert c.is_end_of_word is True


def test_search_exact_returns_true_if_exact_word_is_in_trie(foo_trie):
    assert foo_trie.search_exact('foo') is True


def test_search_exact_returns_false_if_prefix_not_in_trie(foo_trie):
    assert foo_trie.search_exact('bar') is False


def test_search_exact_returns_false_if_prefix_is_in_trie(foo_trie):
    assert foo_trie.search_exact('fo') is False


def test_suggest_returns_empty_list_if_query_less_than_two_char(repo):
    assert repo.suggest('') == []
    assert repo.suggest('f') == []


def test_suggest_returns_empty_list_query_does_not_match_any_prefix(repo):
    assert repo.suggest('bar') == []


def test_suggest_returns_suggestions(repo):
    index = repo._char_to_index('f')
    assert repo.root.children[index] is not None
    result = repo.suggest('fo')
    assert len(result) > 0


def test_suggest_returns_only_words_that_begin_with_query(repo):
    result = repo.suggest('fo')
    assert all(list(map(lambda x: x.startswith('fo'), result)))


def test_suggest_returns_words_in_lexicographic_order(repo):
    result = repo.suggest('fo')
    assert result == sorted(result)


def test_suggest_results_upper_bounded_by_limit(repo):
    repo.suggestions_limit = 3
    result = repo.suggest('fo')
    assert len(result) <= 3


def test_suggest_starts_at_prev_query_root(repo):
    repo.suggest('food')
    prev_loops = repo.loops_this_search
    repo.suggest('foods')
    curr_loops = repo.loops_this_search
    assert curr_loops < prev_loops
