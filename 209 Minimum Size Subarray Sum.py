class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        w = 0
        ret = n+1
        while r < n:
            # extend
            while w < target and r < n:
                w += nums[r]
                r += 1
            while w >= target:
                w -= nums[l]
                l += 1
            ret = min(ret, r-l+1)
        if ret == n+1:
            return 0
        return ret
