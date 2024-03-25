class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = [x - 1 for x in nums]
        ret = []
        for x in range(len(nums)):
            firstF = True
            while x != nums[x]:
                tmp = nums[x]
                if firstF:
                    firstF = False
                    nums[x] = None
                else:
                    nums[x] = x
                x = tmp
                if x is None:
                    break
                if x == nums[x]:
                    ret.append(x+1)
        return ret
