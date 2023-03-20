class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary2:  # trie

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            c = ord(c)-ord('a')
            if not node.children[c]:
                node.children[c] = Node()
            node = node.children[c]
        node.isLeaf = True
    
    def helper(self, node, word):
        if not word:
            return node.isLeaf
        if word[0] == '.':
            for c in range(26):
                if node.children[c] and self.helper(node.children[c], word[1:]):
                    return True
            return False
        c = ord(word[0])-ord('a')
        if node.children[c]:
            return self.helper(node.children[c], word[1:])
        return False
            

    def search(self, word: str) -> bool:
        return self.helper(self.root, word)

class WordDictionary:
    def __init__(self):
        self.ht = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.ht[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.ht[len(word)]

        for w in self.ht[len(word)]:
            for i, char in enumerate(word):
                if  char != w[i] and char != '.':
                    break
            else:
                return True
        return False
