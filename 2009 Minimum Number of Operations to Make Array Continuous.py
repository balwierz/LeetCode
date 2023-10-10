def minOperations(self, nums: List[int]) -> int:
    n, nums, nCov, j = len(nums), sorted(set(nums)), 0, 0
    for i, val in enumerate(nums):
        while j<len(nums) and nums[j] - val < n:
            j += 1
        nCov = max(nCov, j-i)
    return n - nCov
