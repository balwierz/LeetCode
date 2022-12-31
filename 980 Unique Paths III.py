class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numUnvisited = sum(sum(grid[i][j] == 0 for j in range(n)) for i in range(m)) + 1
        #print(numUnvisited)
        ret = 0
        def dfs(x,y):
            nonlocal numUnvisited
            nonlocal ret
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                #print("reached ", numUnvisited)
                if numUnvisited == 0:
                    ret += 1  # found a path
                return
            grid[x][y] = -1
            numUnvisited -= 1
            for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                dfs(x+dx, y+dy)
            grid[x][y] = 0
            numUnvisited += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        return ret
