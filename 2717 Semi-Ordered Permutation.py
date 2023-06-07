class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        return nums.index(1) + n - 1 - nums.index(n) - int(nums.index(1) > nums.index(n))
