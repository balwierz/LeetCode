mod = 12345
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ret = [[1] * n for _ in range(m)]
        def mul(a, b):
            return a * b % mod
        left = [list(accumulate(row, func=mul, initial=1)) for row in grid]
        right = [list(accumulate(reversed(row), func=mul, initial=1)) for row in grid]
        bottom = list(accumulate([left[i][-1] for i in range(m-1, -1, -1)], func=mul, initial=1))
        top = 1
        for i in range(m):
            for j in range(n):
                ret[i][j] = top * bottom[m-1-i] * left[i][j] * right[i][n-1-j] % mod
            top = top * left[i][-1] % mod
        return ret
        

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        vals = arr = list(chain(*grid))
        mul = lambda x, y : x * y % mod 

        pref = list(accumulate(arr,       mul, initial=1))
        suff = list(accumulate(arr[::-1], mul, initial=1))[::-1]

        ans = [p*s % mod for p,s in zip(pref,suff[1:])]
        return list(zip(*[iter(ans)] * n))
