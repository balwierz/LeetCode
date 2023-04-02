class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        a = sorted([nums1[0], nums2[0]])
        b = set(nums1).intersection(set(nums2))
        if b:
            return sorted(b)[0]
        return 10*a[0] + a[1]
        
