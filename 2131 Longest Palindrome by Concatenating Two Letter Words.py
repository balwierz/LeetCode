class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ret = 0
        d = defaultdict(int)
        for w in words:
            r = w[1] + w[0]
            if r in d and d[r] > 0:
                ret += 4
                d[r] -= 1
            else:
                d[w] += 1
        for w in d:
            if d[w] == 1 and w[0] == w[1]:
                return ret + 2
        return ret
