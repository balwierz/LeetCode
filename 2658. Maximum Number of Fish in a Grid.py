class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            nonlocal cnt
            cnt += grid[r][c]
            grid[r][c] = 0
            for a, b in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if a < 0 or a == m or b < 0 or b == n or grid[a][b] == 0:
                    continue
                dfs(a, b)
        ret = 0
        for i in range(m):
            for j in range(n):
                cnt = 0
                if grid[i][j]: dfs(i, j)
                ret = max(ret, cnt)
        return ret
        
