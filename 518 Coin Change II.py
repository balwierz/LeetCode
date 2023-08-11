class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = [c for c in coins if c <= amount]
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins.sort(reverse=True)
        
        for coin in coins:
            dp[coin] = 1
            for i in range(coin, amount - coin + 1):
                dp[i+coin] += dp[i]

        return dp[-1]

class Solution3:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(key=lambda x:-x)
        dp = [0] * (amount+1)
        dp[0] = 1 
        for coin in coins:
            for am in range(1,amount+1):
                if am >= coin:
                    dp[am] += dp[am-coin]
        return dp[-1]


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(key=lambda x:-x)
        @cache
        def nWays(idx, amount):
            if idx == len(coins) and amount == 0:
                return 1
            if idx == len(coins):
                return 0
            thisVal = 0
            ret = 0
            while thisVal <= amount:
                ret += nWays(idx+1, amount-thisVal)
                thisVal += coins[idx]
            return ret
        return nWays(0, amount)
