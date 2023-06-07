class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        negs = sorted([x for x in nums if x < 0])
        poss = [x for x in nums if x > 0]
        negs = negs[0:(len(negs)//2*2)]
        if len(negs) == 0 and len(poss) == 0:
            return 0
        ret = 1
        for x in negs:
            ret *= x
        for x in poss:
            ret *= x
        return ret
