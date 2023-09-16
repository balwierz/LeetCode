def minimumEffortPath(self, h: List[List[int]]) -> int:

    m, n = len(h), len(h[0])

    prio = [(0,0,0)] # val, i, j

    ret = 0

    visited = [[False] * n for _ in range(m)]

    while True:

        v, i, j = heapq.heappop(prio)

        if visited[i][j]:

            continue

        visited[i][j] = True

        ret = max(ret, v)

        if i == m - 1 and j == n - 1:

            return ret

        for a, b in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):

            if a >= 0 and a < m and b >= 0 and b < n and not visited[a][b]:

                heapq.heappush(prio, (abs(h[a][b] - h[i][j]), a, b))
