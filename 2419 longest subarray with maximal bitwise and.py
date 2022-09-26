class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ret = 0
        thisLen = 0
        for num in nums:
            if num == m:
                thisLen += 1
                ret = max(ret, thisLen)
            else:
                thisLen = 0
        return ret
