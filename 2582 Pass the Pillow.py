class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= (2*n-2)
        return time+1 if time <= n-1 else 2*n - 1 - time
