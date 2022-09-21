class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumEven = sum([even for even in nums if even % 2 == 0])
        ret = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                sumEven -= nums[index]
            nums[index] += val
            if(nums[index] % 2 == 0):
                sumEven += nums[index]
            ret.append(sumEven)
        return ret
