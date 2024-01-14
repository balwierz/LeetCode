class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums).values()
        x = max(c)
        y = list(c).count(x)
        return x * y
