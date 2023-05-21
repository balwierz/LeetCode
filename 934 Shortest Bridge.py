class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # find first land:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    break
            else:
                continue
            break
        # mark the whole island: assign 2
        q = deque()
        q.append((i, j,))
        grid[i][j] = 2
        q2 = deque()
        q2.append((i, j, 0))  # last coordinate is distance
        while(q):
            i, j = q.popleft()
            for x, y in ((i-1,j), (i+1, j), (i, j-1), (i, j+1)):
                if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x,y))
                    q2.append((x,y,0))
        # run bfs from island 2
        while(q2):
            i, j, dist = q2.popleft()
            for x, y in ((i-1,j), (i+1, j), (i, j-1), (i, j+1)):
                if x >= 0 and x < n and y >= 0 and y < n:
                    if grid[x][y] == 1:  # we reached the island
                        return dist
                    elif grid[x][y] == 0:
                        grid[x][y] = 2
                        q2.append((x, y, dist+1))
