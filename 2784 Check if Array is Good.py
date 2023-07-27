class Solution:
    def isGood(self, nums: List[int]) -> bool:
        c = Counter(nums)
        m = max(c.keys())
        if c[m] != 2: return False
        for i in range(1, m):
            if c[i] != 1:
                return False
        return True
