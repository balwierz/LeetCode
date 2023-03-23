class Solution:
    def makeConnected(self, n: int, con: List[List[int]]) -> int:
        if len(con) < n - 1: return -1
        visited = [False] * n
        nComponents = 0
        adj = [[] for _ in range(n)]
        for a, b in con:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node):
            visited[node] = True
            for neigh in adj[node]:
                if not visited[neigh]:
                    dfs(neigh)
        for node in range(n):
            if not visited[node]:
                nComponents += 1
                dfs(node)

        return nComponents - 1
