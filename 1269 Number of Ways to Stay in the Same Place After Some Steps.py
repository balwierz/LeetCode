MOD = 1000_000_007 

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        n = arrLen if steps >= arrLen*2 else steps//2 + 1
        data = [0] * n
        data[0] = 1
        for _ in range(steps):
            c = data.copy()
            data[0] += c[1]
            data[-1] += c[-2]
            data[0] %= MOD
            data[-1] %= MOD
            for i in range(1, n-1):
                data[i] += c[i-1] + c[i+1]
                data[i] %= MOD
        return data[0]
        
