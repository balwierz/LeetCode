class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i = 0
        j = 0
        ret = 0
        best = 0
        for x in range(1, len(nums)-1):
            if nums[x] < nums[j]:
                j = x
                best = max(best, nums[i] - nums[x])
            elif nums[x] > nums[i]:
                i = x
                j = x
            ret = max(ret, best * nums[x+1])
        return ret
        
