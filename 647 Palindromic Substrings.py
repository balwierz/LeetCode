class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def odd(pos):
            ret = 1
            l = pos-1
            r = pos+1
            while l>=0 and r<n:
                if s[l] == s[r]:
                    ret += 1
                    l -= 1
                    r += 1
                else:
                    break
            return ret
        def even(pos):
            ret = 0
            l = pos-1
            r = pos
            while l>=0 and r<n:
                if s[l] == s[r]:
                    ret += 1
                    l -= 1
                    r += 1
                else:
                    break
            return ret
        ret = 0
        for pos in range(n):
            ret += odd(pos)
        for pos in range(1, n):
            ret += even(pos)
        return ret
