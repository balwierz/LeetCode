class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[nums[j] for j in range(len(nums)) if (1 << j) & i] for i in range(2**len(nums))]
