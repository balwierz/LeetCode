class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        count = 1
        lag = 1
        i = 1
        while i<n:
            if nums[i] != prev:
                count = 1
                nums[lag] = nums[i]
                prev = nums[i]
                lag += 1
            elif count == 1:
                count = 2
                nums[lag] = nums[i]
                lag += 1
            i += 1
        return lag                
            
