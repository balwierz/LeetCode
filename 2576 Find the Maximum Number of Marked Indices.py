class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        j = n//2
        ret = 0
        for i in range(n//2):
            while j<n and nums[j] < 2 * nums[i]:
                j += 1
            if j<n:
                ret += 2
                j += 1
            elif j==n:
                break
        return ret
