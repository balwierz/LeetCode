class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        w = [[[0,0] for w in range(2)] for q in range(2)]
        # 0 0 0: 0
        w[0][0][1] = 1
        w[0][1][0] = 1
        # 0 1 1: 0
        w[1][0][0] = 1
        # 1 0 1: 0
        w[1][1][0] = 2
        # 1 1 1: 0
        ret = 0
        for _ in range(30):
            ret += w[a&1][b&1][c&1]
            a >>= 1
            b >>= 1
            c >>= 1
        return ret
