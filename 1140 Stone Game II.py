class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        total = sum(piles)
        endSum = []
        for x in piles:
            endSum.append(total)
            total -= x
        print(endSum)
        @cache
        def strategy(a, m):
            if (n-a) <= 2*m: # if possible to take all
                return endSum[a]
            ret = 0
            for i in range(a+1, a+2*m+1):
                ret = max(ret, endSum[a] - strategy(i, max(m, i-a)))
            return ret
        
        return strategy(0, 1)
