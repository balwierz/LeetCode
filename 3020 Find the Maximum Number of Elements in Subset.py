class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        ret = c[1] if c[1] & 1 else c[1] - 1
        del c[1]
        @cache 
        def helper(x):
            return c[x] if c[x] < 2 else 1 + helper(x*x)
        return max(ret, max(helper(x) for x in nums) * 2 - 1)
