class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        c = list(abs(ord(a)-ord(b)) for a, b in zip(s, t))
        l = 0
        cost = 0
        ret = -1
        for r in range(len(s)):
            cost += c[r]
            while l <= r and cost > maxCost:
                cost -= c[l]
                l += 1
            ret = max(ret, r-l)
        return ret + 1
