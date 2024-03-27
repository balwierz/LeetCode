class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        cum = 1
        ret = 0
        l = 0
        for r, x in enumerate(nums):
            cum *= x
            while l <= r and cum >= k:
                cum //= nums[l]
                l += 1
            ret += r - l + 1
        return ret 
