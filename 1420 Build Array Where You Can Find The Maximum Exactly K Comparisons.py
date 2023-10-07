MOD = 1_000_000_007
class Solution:
    @cache
    def num(self, n, mx, k):
        ret = 0
        # mx is the largest value encountered in the array
        if n == 1:
            if k != 1:
                return 0
            return 1
        if k > n:
            return 0
        # last one is mx: 
        for mxi in range(1, mx):
            ret += self.num(n-1, mxi, k-1)
            ret %= MOD
        ret += self.num(n-1, mx, k) * mx
        #print("n", n, "mx", mx, "k", k, ":", ret)
        return ret % MOD
    def numOfArrays(self, n, m, k):
        return sum(self.num(n, mi, k) for mi in range(1, m+1)) % MOD
