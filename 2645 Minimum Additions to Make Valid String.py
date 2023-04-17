class Solution:
    def addMinimum(self, word: str) -> int:
        ret = 0
        s = "abc"
        i = 0
        for c in word:
            while s[i] != c:
                ret += 1
                i = (i+1) % 3
            i = (i+1) % 3
        if word[-1] == 'b': ret += 1
        if word[-1] == 'a': ret += 2
        return ret
