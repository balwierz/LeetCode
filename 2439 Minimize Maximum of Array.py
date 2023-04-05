class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        lvl, total = 0, 0
        for i, num in enumerate(nums):
            total += num
            lvl = max(lvl, (total + i) // (i+1))
        return lvl
