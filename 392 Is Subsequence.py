class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tI = 0
        for l in s:
            while tI < len(t) and t[tI] != l:
                tI += 1
            if tI == len(t):
                return False
            tI += 1
        return True
