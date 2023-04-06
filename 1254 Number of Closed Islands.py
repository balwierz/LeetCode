class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
             nonlocal grid
             for a, b in ((i-1,j), (i+1, j), (i, j-1), (i, j+1)):
                 if a>0 and a<m and b>0 and b<n and grid[a][b] == 0:
                     grid[a][b] = 5
                     dfs(a,b)
        for j in range(n):
            if grid[0][j] == 0: dfs(0,j)
            if grid[m-1][j] == 0: dfs(m-1,j)
        for i in range(1, m-1):
            if grid[i][0] == 0: dfs(i, 0)
            if grid[i][n-1] == 0: dfs(i, n-1)
        
        ret = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    ret += 1
                    dfs(i, j)
        return ret
