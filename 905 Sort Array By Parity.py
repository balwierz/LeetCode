class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        i, j = 0, len(nums) - 1
        for x in nums:
            if x % 2 == 0:
                ret[i] = x
                i += 1
            else:
                ret[j] = x
                j -= 1
        return ret
        
