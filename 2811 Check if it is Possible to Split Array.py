class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        return len(nums) <= 2 or max(map(sum, pairwise(nums))) >= m
