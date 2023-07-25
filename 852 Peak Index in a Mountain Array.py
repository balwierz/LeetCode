class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 2
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid+1] - arr[mid] > 0:
                l = mid
            else:
                r = mid
        return r
