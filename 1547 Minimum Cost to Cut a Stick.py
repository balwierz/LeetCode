class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        @cache
        def best(i, j): # i, j are indices of cuts
            if i + 1 == j:
                return 0
            ret = 999999999
            for k in range(i+1, j):
                ret = min(ret, best(i,k) + best(k,j))
            return ret + cuts[j] - cuts[i]
        return best(0, len(cuts)-1)
