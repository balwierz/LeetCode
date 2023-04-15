class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (n+1) for _ in range(k+1)]  # [k][n]
        for pileI in range(n):
            cumsum = 0
            for nElem in range(min(k+1, 1+len(piles[pileI]))):  # num elem taken from the last pile
                for nElemPrev in range(k+1-nElem):            # num elem taken from previous piles
                    thisElem = nElem + nElemPrev              # num elem total
                    dp[thisElem][pileI] = max(dp[thisElem][pileI], dp[nElemPrev][pileI-1] + cumsum)
                if nElem < len(piles[pileI]):
                    cumsum += piles[pileI][nElem]
        return dp[k][n-1]
