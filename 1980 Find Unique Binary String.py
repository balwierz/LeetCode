class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        fmt = '0' + str(len(nums[0])) + 'b'
        nums = set(nums)
        for i in range(0, 17):
            if format(i, fmt) not in nums:
                return format(i, fmt)
