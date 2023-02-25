class Solution:
    def maxProfit(self, p: List[int]) -> int:
        lowest = 999999
        ret = 0
        for x in p:
            ret = max(ret, x-lowest)
            lowest = min(lowest, x)
        return ret
