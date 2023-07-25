class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        x = 15625
        len2repr = dict()
        while x>0:
            r = bin(x)[2:]
            len2repr[len(r)] = r
            x //= 5
        ll = sorted(list(len2repr.keys()))
        def minNum(s):
            if len(s) == 0:
                return 0
            ret = 999
            for l in ll:
                if l > len(s):
                    break
                if s[:l] == len2repr[l]:
                    ret = min(ret, 1 + minNum(s[l:]))
            return ret
        ret = minNum(s)
        return ret if ret < 999 else -1
