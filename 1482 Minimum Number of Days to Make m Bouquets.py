import numpy as np

class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        if m*k > len(b):
            return -1
        b = np.array(b)
        def check(day):
            nonlocal b, m
            numBouq = 0
            for val, elems in groupby(b <= day):
                if val:
                    numBouq += len(list(elems)) // k
            return numBouq >= m
        
        l, r = 0, np.max(b)
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid

        return r
