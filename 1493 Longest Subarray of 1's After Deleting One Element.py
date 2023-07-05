class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(1 == n for n in nums):
            return len(nums) - 1
        best2 = 0
        lastDig = 0
        lastLen = 0
        thisLen = 0
        for num in nums:
            if num == 0:
                best2 = max(best2, lastLen + thisLen)
                lastLen = thisLen
                thisLen = 0
            else: # num == 1
                thisLen += 1
            lastDig = num
        best2 = max(best2, lastLen + thisLen)
        return best2
