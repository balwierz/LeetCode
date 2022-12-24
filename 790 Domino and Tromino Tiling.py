class Solution:
    def numTilings(self, n: int) -> int:
        flatDp = [0 for _ in range(n+2)]
        topDp  = [0 for _ in range(n+2)]
        flatDp[0] = 1
        for i in range(0, n):
            flatDp[i] %= 1000000007
            topDp[i]  %= 1000000007
            flatDp[i+1] += flatDp[i]
            flatDp[i+2] += flatDp[i] + topDp[i]
            topDp[i+1]  += 2*flatDp[i] + topDp[i]
        return flatDp[n] % 1000000007
