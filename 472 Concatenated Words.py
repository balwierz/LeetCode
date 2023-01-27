class Node:
    def __init__(self):
        self.isEnd = False
        self.child = [None] * 26

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        root = Node()
        ret = []
        for word in words:
            adder = root
            checkers = [root]
            for letter in word:
                newCheckers = []
                idx = ord(letter)-ord('a')
                for checker in checkers:
                    child = checker.child[idx]
                    if child:   # child exists
                        if child.isEnd:
                            newCheckers.append(root)
                        newCheckers.append(child)
                if not adder.child[idx]:
                    adder.child[idx] = Node()
                adder = adder.child[idx]
                checkers = newCheckers
            if any([c == root for c in checkers]):
                ret.append(word)   # success
            adder.isEnd = True
        return ret
                
