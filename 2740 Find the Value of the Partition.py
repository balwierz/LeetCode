class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        return min(itertools.starmap(operator.sub, itertools.pairwise(sorted(nums, reverse=True))))
        
        
        nums.sort()
        ret = float('inf')
        for i in range(1, len(nums)):
            ret = min(ret, nums[i] - nums[i-1])
        return ret
