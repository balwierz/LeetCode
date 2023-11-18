class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = 1
        lagI = 0  # first index taken
        used = 0  # number of additions used
        lvl = nums[0]
        for i, x in enumerate(nums):
            # now x is the level to which values have grown to from lagI
            rise = x - lvl
            used += rise * (i - lagI)
            while used > k:
                used -= x - nums[lagI]
                lagI += 1
            ret = max(ret, i - lagI + 1) 
            lvl = x
        return ret

    # I dont know why this works:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        A = nums
        i = 0
        A.sort()
        for j in range(len(A)):
            k += A[j]
            if k < A[j] * (j - i + 1):
                k -= A[i]
                i += 1
        return j - i + 1
