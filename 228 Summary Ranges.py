class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        prev = nums[0]
        start = nums[0]
        ret = []
        for num in nums[1:]+[nums[-1]+2]:
            if prev + 1 != num:
                if prev == start:
                    ret.append(str(prev))
                else:
                    ret.append(str(start)+"->"+str(prev))
                start = num
            prev = num
        return ret
