class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        a = b = s = ret = 0
        for x in nums:
            s += x
            if s > b:
                b = s
            if s < a:
                a = s
        return b - a
