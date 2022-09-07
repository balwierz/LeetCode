class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        lag = 1
        n = len(nums)
        while i<n:
            if nums[i] != nums[i-1]:
                nums[lag] = nums[i]
                lag += 1
            i += 1
        return lag
