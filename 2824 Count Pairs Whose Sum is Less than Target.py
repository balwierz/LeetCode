class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        nums.sort()
        ret = 0
        while i<j:
            while i<j and nums[j] + nums[i] >= target:
                j -= 1
            ret += j-i
            i += 1
        return ret
