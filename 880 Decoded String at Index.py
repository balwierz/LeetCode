class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        k -= 1 # wtf counting from 1
        lenSt = []
        curLen = 0
        for c in s:
            if c.isdigit():
                curLen *= int(c)
            else:
                curLen += 1
            lenSt.append(curLen)
        i = len(s)
        while i:
            i -= 1
            if s[i].isdigit():
                k %= lenSt[i-1]
            elif k == lenSt[i]-1:
                return s[i]        
