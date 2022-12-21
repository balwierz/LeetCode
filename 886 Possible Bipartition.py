class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        neigh = [[] for _ in range(n)]
        for a, b in dislikes:
            a -= 1
            b -= 1
            neigh[a].append(b)
            neigh[b].append(a)
        col = [-1 for _ in range(n)]
        def dfs(node, c):
            if col[node] == 1-c:
                return False
            if col[node] == c:
                return True
            col[node] = c
            for v in neigh[node]:
                if not dfs(v, 1-c):
                    return False
            return True
        for s in range(n):
            if col[s] != -1:
                continue
            if not dfs(s, 0):
                return False
        return True
