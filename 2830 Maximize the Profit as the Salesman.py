class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        i, dp = 0, [0] * (n+1)
        offers.sort(key=lambda x: x[1])
        for end in range(n):
            dp[end] = dp[end-1]
            while i < len(offers) and offers[i][1] == end:
                dp[end] = max(dp[end], offers[i][2] + dp[offers[i][0]-1])
                i += 1
        return dp[-2]
