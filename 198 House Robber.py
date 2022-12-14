class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return max(nums)
        nums[2] += nums[0]
        for h in range(3, n):
            nums[h] += max(nums[h-2], nums[h-3])
        return max(nums[-2], nums[-1])
