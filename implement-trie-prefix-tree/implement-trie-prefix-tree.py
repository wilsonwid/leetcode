class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                newnode = TrieNode(c)
                node.children[c] = newnode
                node = newnode
        node.is_end = True
        node.counter += 1


    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}
