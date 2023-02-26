class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        right = [0] * len(nums)
        ret = [0] * len(nums)
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] + nums[i+1]
        ret[0] = right[0]
        left = 0
        for i in range(1, len(nums)):
            left += nums[i-1]
            ret[i] = abs(left - right[i])
        return ret
