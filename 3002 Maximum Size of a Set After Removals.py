class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1) // 2
        a, b = set(nums1), set(nums2)
        y = a.intersection(b)
        x, z = a-y, b-y
        unique = min(m, len(x)) + min(m, len(z))
        common = min(2*m - unique, len(y))
        return unique + common
