class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es, ds = 0, 0
        for num in nums:
            es += num
            while num:
                num, rem = divmod(num, 10)
                ds += rem
        return abs(es - ds)
