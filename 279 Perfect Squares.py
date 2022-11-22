squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
squaresSet = set(squares)
dp = [0] * (10001)

class Solution:
    def numSquares2(self, n: int) -> int:  ## time exceeded
        dp = [99999] * (n+1)
        for i in range(1, n+1):
            if i in squaresSet:
                dp[i] = 1
                continue
            for j in range(1, i//2+1):
                dp[i] = min(dp[i], dp[j] + dp[i-j])
        return dp[n]
    
    def numSquares3(self, n: int) -> int:  # 200ms
        if n < 4:
            return n
        if(dp[n]):
            return dp[n]

        ptr = bisect.bisect(squares, n) - 1
        ret = 999999
        while(ptr):
            ret = min(ret, 1 + self.numSquares(n-squares[ptr]))
            ptr -= 1
        dp[n] = ret
        return ret
    
    # lagrange and legendre four-square and three-square theorems
    #https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem

    def numSquares(self, n: int):  # 60ms
        if n in squaresSet:
            return 1
        
        # four-square and three-square theorems
        while not n & 0b11:
            n >>= 2      # reducing the 4^k factor from number

        if n & 0b111 == 0b111: # mod 8
            return 4

        # check if the number can be decomposed into sum of two squares
        for num in range(1, floor(sqrt(n)) + 1):
            if (n - num * num) in squaresSet:
                return 2
        # bottom case from the three-square theorem
        return 3
