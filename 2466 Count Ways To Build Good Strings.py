class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        if zero > one:  zero, one = one, zero
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(high+1):
            if dp[i] == 0:
                continue
            if i+one <= high:
                dp[i+one] += dp[i]
            if i+zero <= high:
                dp[i+zero] += dp[i]
            else:
                break
        return sum(dp[low:high+1]) % 1_000_000_007
