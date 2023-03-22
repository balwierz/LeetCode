def minScore(self, n: int, roads: List[List[int]]) -> int:
    adj = [[] for _ in range(n+1)]
    for a, b, d in roads:
        adj[a].append((b, d))
        adj[b].append((a, d))
    visited = [False] * (n+1)
    ret = 999999999

    def dfs(node):
        nonlocal ret
        visited[node] = True
        for neigh, dist in adj[node]:
            if dist < ret: ret = dist
            if not visited[neigh]:
                dfs(neigh)
    dfs(1)
    return ret
