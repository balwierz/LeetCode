class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = Counter(nums)
        nums[:] = [0] * a[0] + [1] * a[1] + [2] * a[2]
