class Solution:
    def maxDotProduct(self, n1: List[int], n2: List[int]) -> int:     
        dp = [[0] * len(n2) for _ in range(len(n1))]
        dp[0][0] = n1[0] * n2[0]
        for i in range(1, len(n1)):
            dp[i][0] = max(dp[i-1][0], n1[i]*n2[0])
        for j in range(1, len(n2)):
            dp[0][j] = max(dp[0][j-1], n1[0]*n2[j])
        for i in range(1, len(n1)):
            for j in range(1, len(n2)):
                dp[i][j] = max(n1[i]*n2[j], dp[i-1][j-1] + n1[i]*n2[j], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        
