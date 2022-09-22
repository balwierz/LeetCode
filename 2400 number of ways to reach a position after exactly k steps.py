newtonMemo = [[int(0)] * 1001 for _ in range(1001)]

def newton(n, k):
    if k==0 or n==k:
        return 1
    if newtonMemo[n][k] != 0:
        return newtonMemo[n][k]
    ret = newton(n-1, k) + newton(n-1, k-1)
    newtonMemo[n][k] = ret
    return ret

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        stepsRight = abs(endPos - startPos)
        if (k - stepsRight) % 2 == 1 or stepsRight > k:
            return 0
        stepsRight += (k - stepsRight) // 2
        #return newton(k, stepsRight) % int(1e9+7)
        return comb(k, stepsRight) % int(1e9+7)
