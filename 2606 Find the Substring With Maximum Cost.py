class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        realVal = [0] * ord('a') + list(range(1, 27))
        for c, v in zip(chars, vals):
            realVal[ord(c)] = v
        ret = 0
        dp = 0
        for c in s:
            dp = max(0, realVal[ord(c)], dp + realVal[ord(c)])
            ret = max(ret, dp)
        return ret
