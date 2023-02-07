class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        cum = [0] * (n+1)
        c = 0
        for i, w in enumerate(words):
            if (w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'u') and (w[-1] == 'a' or w[-1] == 'e' or w[-1] == 'i' or w[-1] == 'o' or w[-1] == 'u'):
                c += 1
            cum[i] = c
        cum[n] = 0   # used as -1 coordinate
        ret = []
        for a, b in queries:
            ret.append(cum[b] - cum[a-1])
        return ret
