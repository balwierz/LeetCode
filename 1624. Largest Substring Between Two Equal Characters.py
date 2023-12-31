class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ret = 0
        for i, x in enumerate(s):
            if x in first:
                ret = max(ret, i-first[x])
            else:
                first[x] = i
        return ret-1
