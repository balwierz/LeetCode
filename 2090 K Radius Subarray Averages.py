class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2*k + 1:
            return [-1] * len(nums)
        ret = [-1] * k
        s = sum(nums[0:(2*k+1)])
        ret.append(s//(2*k+1))
        for j in range(2*k+1, len(nums)):
            s -= nums[j-2*k-1]
            s += nums[j]
            ret.append(s//(2*k+1))
        ret.extend([-1] * k)
        return ret
