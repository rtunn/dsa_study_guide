# Trie

Trie is a tree structure that stores characters of strings. Common prefixes of strings share the same branch.

## Implementation

The Trie will need to store nodes, so create a TrieNode data structure that stores children and a boolean noting if the node is the end of a word.

The Trie data structure will be initialized with a root == empty node

### Inserting Words

The Trie must implement an insert method. For i from 0 -> |word| - 1, the insert method checks if the i-th character of word is present in the current node's children. The current node begins at the Trie's root node.

If the character is present, the child node becomes the current node.

If the character is not present, a new empty node is created and added to the current node's children. Then the new child node becomes the parent node

The last node is marked as being the end of a word.

### Searching Words

The Trie must implement a search method. For each character in the word, if the character is present in the current node's children, the child node becomes the current node.

If no child node labeled as the character is present, the search returns false.

If all characters are present, the search returns whether or not the final node is the end of a word.

## Time Complexity

### Building the Trie

Each insert operation does O(L) work where L is the length of the word

We perform insert n times where n is the number of words.

Since L may vary from word to word, we can instead consider the character count of all words S.

Building the Trie has a running time of O(S)

### Searching The Trie

The search operation must check every character in the word for a running time of O(L) where L is the length of the word.

### Finding All Words With A Common Prefix

The worst case is when all words share the prefix of the search query. This results in a running time of O(S) where S is the number of characters in all words in the Trie.

### Finding K Words With A Common Prefix, i.e. Autocomplete

If we only need to find K words with a common prefix the worse case will be O(S) when K is equal to N, the number of words in the Trie.

For K much smaller than N, the worst case is when all K words have length U, the length of the longest word in the Trie. O(K\*U)

## Space Complexity

Since the TrieNode children are stored as an array with size equal to the alphabet size, our space complexity is O(alphabet size _ U _ N) where U is the length of the longest word and N is the number of words in the Trie.
