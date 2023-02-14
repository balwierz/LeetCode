class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(val, k):
            last = 0    # previous elemnt in the array was not used
            for home in nums:
                if not last and home <= val:
                    k -= 1
                    if k == 0:
                        return True
                    last = 1   # used
                else:
                    last = 0   # not useed
            return False
        lo, hi = 0, max(nums)
        while lo != hi:
            if lo + 1 == hi:
                break
            cur = (lo + hi) // 2
            if check(cur, k):
                hi = cur
            else:
                lo = cur
        return hi
