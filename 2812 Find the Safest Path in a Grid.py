def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return 0
    dist2coords = defaultdict(list)
    q = deque()
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                q.append([r,c])
                dist2coords[1].append([r,c])
    step = 1
    while q:
        step += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            if r > 0 and grid[r-1][c] == 0:
                grid[r-1][c] = step
                q.append([r-1, c])
            if r+1 < m and grid[r+1][c] == 0:
                grid[r+1][c] = step
                q.append([r+1, c])
            if c > 0 and grid[r][c-1] == 0:
                grid[r][c-1] = step
                q.append([r, c-1])
            if c+1 < n and grid[r][c+1] == 0:
                grid[r][c+1] = step
                q.append([r, c+1])
    dist = min(grid[0][0], grid[m-1][n-1])
    for r in range(m):
        for c in range(n):
            d = min(dist, grid[r][c])
            grid[r][c] = d
            dist2coords[d].append([r, c])
    parent = [[[r, c] for c in range(n)] for r in range(m)]

    def root(a, b):
        while parent[a][b] != [a, b]:
            parent[a][b] = parent[parent[a][b][0]][parent[a][b][1]]
            a, b = parent[a][b]
        return [a, b]

    for dist in range(dist, 0, -1):
        for r, c in dist2coords[dist]:
            for y, x in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if y >= 0 and y < m and x >= 0 and x < n:
                    if grid[y][x] >= dist and root(y, x) != root(r, c):
                        y, x = root(y, x)
                        parent[y][x] = root(r, c)
        if root(0, 0) == root(m-1, n-1):
            return dist-1
    return 0
