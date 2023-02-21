class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums += [999999]   # now it is even length
        def unequal(i):
            return nums[i] != nums[i+1]
        if unequal(0): return nums[0]
        l, r = 0, (len(nums)-2) // 2
        while l != r and l+1 != r:
            mid = (l+r) & 0xFFFFFFE   # in 2x coordinates
            if unequal(mid):
                r = mid >> 1
            else:
                l = mid >> 1
        return nums[r<<1]
