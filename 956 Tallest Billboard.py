class Solution:
    def tallestBillboard2(self, rods: List[int]) -> int:
        dp = {0: 0}
        for x in rods:
            for d, y in list(dp.items()):
                dp[d + x] = max(dp.get(x + d, 0), y)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        return dp[0]

    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(rods):
            dp = {0:0}
            for r in rods:
                for d,h in list(dp.items()):
                    dp[d+r] = max(dp.get(d+r,0), h)
                    dp[abs(d-r)] = max(dp.get(abs(d-r),0), h+min(d,r))
            return dp
        dp1,dp2 = helper(rods[:len(rods)//2]), helper(rods[len(rods)//2:])
        return max(h+d+dp2[d] for d,h in dp1.items() if d in dp2)
