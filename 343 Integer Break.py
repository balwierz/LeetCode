class Solution:
    def integerBreak(self, n: int) -> int:
        dp =  [0, 1]
        for i in range(2, n+1):
            dp.append(dp[-1])
            for j in range(2, i):
                dp[-1] = max(dp[-1], j * dp[-1-j] )
            if i == n:
                return dp[-1]
            dp[-1] = max(i, dp[-1])
