class Trie:
    def __init__(self, val):
        self.val = val
        self.child = dict()
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie(0)
        for w in words:
            ptr = root
            for letter in w:
                if not letter in ptr.child:
                    ptr.child[letter] = Trie(1)
                else:
                    ptr.child[letter].val += 1
                ptr = ptr.child[letter]
        # compute answers
        ret = []
        for w in words:
            cntr = 0
            ptr = root
            for letter in w:
                ptr = ptr.child[letter]
                cntr += ptr.val
            ret.append(cntr)
        return ret
