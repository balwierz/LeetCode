class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def minCost(startIdx, timeLeft):
            if startIdx == n:
                return inf if timeLeft > 0 else 0
            if timeLeft <= 0:
                return 0
            a = minCost(startIdx+1, timeLeft)  # dont take it
            b = cost[startIdx] + minCost(startIdx+1, timeLeft - time[startIdx] -1)
            #print(startIdx, timeLeft, ":", a, b)
            return min(a, b)
        return minCost(0, n)

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [inf] * n
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n] 
