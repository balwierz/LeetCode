class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        n1 = len(list(1 for x in nums1 if x == 0))
        n2 = len(list(1 for x in nums2 if x == 0))
        d = s2 - s1 + n2 - n1
        ret = s1 + s2 + n2 + n1
        if d < 0:
            d = -d
            n1 = n2
        if n1 > 0:
            return (ret + d) // 2
        else:
            return ret // 2 if d == 0 else -1


        
