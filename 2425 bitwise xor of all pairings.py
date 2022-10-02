    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ret = 0
        if n2 % 2 == 1:
            ret =  reduce(lambda x, y : x^y, nums1)
        if n1 % 2 == 1:
            ret ^= reduce(lambda x, y : x^y, nums2)
        return ret
