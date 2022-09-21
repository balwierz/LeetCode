class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        last = 0
        ret = 1
        thisLen =0
        for c in s:
            if ord(c) == last +1:
               thisLen +=1
               ret = max(ret, thisLen)
            else:
               thisLen = 1
            last = ord(c)
        return ret
