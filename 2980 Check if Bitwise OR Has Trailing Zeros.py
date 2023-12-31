class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return Counter(x&1 for x in nums)[0] > 1
