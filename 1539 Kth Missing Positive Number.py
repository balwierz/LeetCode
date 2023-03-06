class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # left of array:
        if arr[0] - 1 >= k:
            return k
        # right of array
        if arr[n-1] - n < k:
            return k + n
        l, r = 0, n-1
        # bisection
        while l + 1 != r:
            mid = (r+l) // 2
            if arr[mid] - mid - 1 < k:
                l = mid
            else:
                r = mid
        return k + l + 1
