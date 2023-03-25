class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node) -> int:
            visited[node] = True
            ret = 1
            for v in adj[node]:
                if not visited[v]:
                    ret += dfs(v)
            return ret
        
        sizes = []
        for node in range(n):
            if not visited[node]:
                sizes.append(dfs(node))
        
        ret = 0
        for i in range(len(sizes)):
            ret += sizes[i] * (n-sizes[i])
        return ret//2
