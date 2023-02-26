class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        q = [(0, 0, 0)]
        while True:
            t, r, c = heappop(q)
            t += 1
            for i, j in ((r-1,c), (r+1,c), (r, c-1), (r, c+1)):
                if i<0 or i>=m or j<0 or j>=n or grid[i][j] == -1: continue
                when = max(t, grid[i][j] + (1 if (t+grid[i][j])%2 else 0 ) )
                if i == m-1 and j == n-1: return when
                heappush(q, (when, i, j))
                grid[i][j] = -1
