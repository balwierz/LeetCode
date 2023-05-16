class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while True:
            if i >= len(nums):
                return(k)
            if nums[i] != val:
                k += 1
            else:
                p = val
                while i < len(nums) and p == val:
                    p = nums.pop()
                if i < len(nums):
                    nums[i] = p
                    k += 1
            i += 1

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
        
