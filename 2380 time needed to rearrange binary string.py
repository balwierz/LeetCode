import re
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = re.sub("^1*", "", s)
        c = Counter(s)
        n = len(s)
        if c['0'] == 0 or c['1'] == 0:
            return 0
        ret = 0
        startPos = 0
        for i in range(n):
            if s[i] == '1':
                tWait = c['1'] -1 - startPos
                tMove = i - startPos
                startPos += 1
                ret = max(ret, tWait + tMove)
        return ret
