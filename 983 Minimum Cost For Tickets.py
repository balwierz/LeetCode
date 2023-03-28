def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    dp = [0] * 400
    lastDay = 0
    for day in days:
        for day2 in range(lastDay+1, day):
            dp[day2] = dp[lastDay]
        a = costs[0] + dp[day-1]
        b = costs[1] + dp[day-7]
        c = costs[2] + dp[day-30]
        dp[day] = min(a, b, c)
        lastDay = day
    return dp[lastDay]
