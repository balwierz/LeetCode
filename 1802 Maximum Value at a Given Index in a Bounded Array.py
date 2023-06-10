class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n  # now we are building from zero level, not 1
        def integral(maxLvl):
            nonlocal n, index
            ret = 0 #maxLvl
            lvlAt0 = maxLvl - index
            if lvlAt0 <= 0:
                ret += (maxLvl+1) * maxLvl // 2
            else:
                ret += (lvlAt0+maxLvl) * (index+1) // 2
            # right side:
            lvlAtEnd = maxLvl - (n - 1 - index)
            if lvlAtEnd <= 0:
                ret += maxLvl * (maxLvl-1) // 2
            else:
                a = (lvlAtEnd+maxLvl-1) * (n - 1 - index) // 2
                ret += a
            return ret

        l = 0
        r = maxSum+1

        while l+1 < r:
            mid = (l+r) // 2
            if integral(mid) <= maxSum:
                l = mid
            else:
                r = mid
        
        return l+1
