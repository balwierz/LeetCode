class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all((a-b)>=0 for a, b in pairwise(nums)) or all((a-b)<=0 for a, b in pairwise(nums))
        
