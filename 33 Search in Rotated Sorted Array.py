class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the transition:
        n = len(nums)
        l, r = -1, n-1
        while l+1 < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m
        # r is now the start of the original array
        ind = r
        l, r = -1, n-1
        while l+1 < r:
            m = (l+r) // 2
            if nums[(m+ind)%n] >= target:
                r = m
            else:
                l = m
        return (r+ind)%n if nums[(r+ind)%n] == target else -1
