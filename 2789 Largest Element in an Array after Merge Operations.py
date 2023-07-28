class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ret = 0
        prefSum = 0
        for x in nums[::-1]:
            if x > prefSum:
                prefSum = x
            else:
                prefSum += x
            ret = max(ret, prefSum)
        return ret
