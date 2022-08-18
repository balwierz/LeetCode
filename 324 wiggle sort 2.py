class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = sorted(nums)
        #print("".join([str(x) for x in nums2]))
        w = j = (len(nums) + 1) // 2
        ret = []
        i = w-1
        z = w
        if len(nums)  & 1:
            z = w -1
        while(i>=0):
            ret.append(nums2[i])
            if z + i >= w:
                ret.append(nums2[z + i])
            i -= 1
        nums[:] = ret
        
