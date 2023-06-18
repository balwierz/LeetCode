mod = 1_000_000_007
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j):
            a = grid[i][j]
            ret = 1
            for k, l in ((i, j-1), (i, j+1), (i-1, j), (i+1, j)):
                if k>=0 and k<m and l>=0 and l<n and grid[k][l] > a:
                    ret += dfs(k, l) % mod
            return ret % mod
        
        ret = 0
        for i in range(m):
            for j in range(n):
                ret += dfs(i, j) % mod
        return ret % mod
