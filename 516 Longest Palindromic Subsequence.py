def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    if s == s[::-1]: return n
    dp = [0] * n
    ret = 0
    for i in range(n-1, 0, -1):
        c = s[i]
        prev = 0
        for j in range(i):
            prev, dp[j] = dp[j], max(prev + 2 if s[j] == c else 0, dp[j], dp[j-1])
        ret = max(ret, max(dp[:i]), dp[i-1] + int(dp[i-1] == dp[i-2]))
    return ret
