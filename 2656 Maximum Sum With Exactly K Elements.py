class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        ret = 0
        for i in range(k):
            ret += m
            m += 1
        return ret
        
