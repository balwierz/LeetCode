class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ls = 0
        rs = sum(nums)
        bestVal = rs+1  # for sure higher than any possible value
        bestInd = 0
        for i, v in enumerate(nums):
            ls += v
            rs -= v
            if n-i-1 == 0:
                ravg = 0
            else:
                ravg = rs//(n-i-1)
            diff = abs(ls//(i+1) - ravg)
            if diff < bestVal:
                bestVal = diff
                bestInd = i
                if diff == 0:
                    return i
        return bestInd
        
