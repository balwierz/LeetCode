class Solution:
    def isFascinating(self, n: int) -> bool:
        t = str(n)+str(2*n)+str(3*n)
        if len(t) != 9:
            return False
        ts = set(t)
        if len(ts) == 9 and '0' not in ts:
            return True
        return False
