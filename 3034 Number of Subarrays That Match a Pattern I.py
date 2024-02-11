def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
    nums = [(b-a > 0) - (b-a < 0) for a, b in pairwise(nums)]
    return sum(pattern == nums[i:(i+len(pattern))] for i in range(len(nums)-len(pattern)+1))
