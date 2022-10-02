class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, n+1):   # loop over num dice
            ddp = [0] * (target+1)
            for s in range(i, target+1):  # loop over sums
                for die in range(1, min(s+1, k+1)): # loop over die outcomes
                    ddp[s] += dp[s - die]
                ddp[s] %= int(1e9+7)
            dp = ddp
        return dp[target]
