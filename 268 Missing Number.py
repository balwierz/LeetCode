class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(operator.__xor__, chain(nums, range(len(nums)+1)))
