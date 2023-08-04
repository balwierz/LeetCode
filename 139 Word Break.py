class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*len(s) + [True]
        #return map(lambda i: dp[i] = any(dp[j-1] and (s[j:i+1] in wordDict) for j in range(i+1)), range(len(s)))[len(s)-1]
        for i in range(len(s)):
            dp[i] = any(dp[j-1] and (s[j:i+1] in wordDict) for j in range(i+1))
        return dp[len(s)-1]

class Node:
    def __init__(self):
        self.children = dict()   #letter to Node
        self.isEnd = False
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node()
        for w in wordDict:
            node = root
            for letter in w:
                if letter not in node.children:
                    node.children[letter] = Node()
                node = node.children[letter]
            node.isEnd = True
        @cache
        def isPossible(pos):
            if pos == len(s):
                return True
            node = root
            pos2 = pos
            for letter in s[pos:]:
                if letter not in node.children:
                    return False
                node = node.children[letter]
                pos2 += 1
                if node.isEnd:
                    if isPossible(pos2):
                        return True
            return False
        return isPossible(0)
