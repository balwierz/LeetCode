class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        n = 0
        for num in nums:
            if num % 6 == 0:
                n += 1
                s += num
        if n == 0:
            return 0
        return s // n
