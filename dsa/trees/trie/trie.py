import sys


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_node()
        self.suggestions = []
        self.suggestions_limit = sys.maxsize
        self.loops_this_search = 0
        self.prev_query_root = None

    def get_node(self) -> TrieNode:
        return TrieNode()

    def _char_to_index(self, char: str) -> int:
        return ord(char) - 97

    def _index_to_char(self, index: int) -> str:
        return chr(97 + index)

    def insert(self, word: str) -> None:
        parent = self.root
        for char in word:
            index = self._char_to_index(char)
            if not parent.children[index]:
                parent.children[index] = self.get_node()
            parent = parent.children[index]
        parent.is_end_of_word = True

    def search_exact(self, word: str) -> bool:
        parent = self.root
        for char in word:
            index = self._char_to_index(char)
            if not parent.children[index]:
                return False
            parent = parent.children[index]
        return parent.is_end_of_word

    def _populate_suggestions(self, node: TrieNode, prefix: str) -> None:
        self.loops_this_search += 1
        if len(self.suggestions) == self.suggestions_limit:
            return
        if node.is_end_of_word:
            self.suggestions.append(prefix)
        for i in range(len(node.children)):
            if node.children[i] is None:
                continue
            child_char = self._index_to_char(i)
            query = prefix + child_char
            self._populate_suggestions(node.children[i], query)

    def _suggest(self, query: str, start: TrieNode) -> list[str]:
        self.suggestions = []
        if len(query) < 2:
            return self.suggestions

        self.loops_this_search = 0
        if start == self.prev_query_root:
            self._populate_suggestions(start, query)
            return self.suggestions

        parent = start
        for char in query:
            index = self._char_to_index(char)
            if not parent.children[index]:
                return self.suggestions
            parent = parent.children[index]
        self.loops_this_search = len(query)

        # save this node so we don't have to work down the trie
        # when the next character is typed
        # instead we'll use this as our root
        self.prev_query_root = parent

        self._populate_suggestions(parent, query)
        return self.suggestions

    def suggest(self, query: str) -> list[str]:
        start = self.prev_query_root if self.prev_query_root is not None else self.root
        return self._suggest(query, start)


def main():
    trie = Trie()
    words = [
        'foo',
        'food',
        'fool',
        'foods',
        'fools',
        'cats',
        'birds',
        'mice'
    ]
    for word in words:
        trie.insert(word)
    trie.suggestions_limit = 3
    trie.suggest('fo')


if __name__ == '__main__':
    main()
