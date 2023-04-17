class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        return list(accumulate(a+b for a, b in zip(nums, accumulate(nums, max))))
