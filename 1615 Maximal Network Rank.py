class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if n == 1 or len(roads) == 0:
            return 0
        if len(roads) == n*(n-1) // 2:
            return 2*n - 3
        adj = [[False] * n for _ in range(n)]
        deg = [0] * n
        for a, b in roads:
            adj[a][b] = adj[b][a] = True
            deg[a] += 1
            deg[b] += 1
        deg2list = [[] for _ in range(n)]
        for i, d in enumerate(deg):
            deg2list[d].append(i)
        b = None
        #print(deg2list)
        for d in range(n-1, -1, -1):
            if not b and len(deg2list[d]):
                b = d
                if(len(deg2list[d])) >= 2:
                    for i, city1 in enumerate(deg2list[d]):
                        for city2 in deg2list[d][i+1:]:
                            if not adj[city1][city2]:
                                return 2*d
                    return 2*d-1
            elif len(deg2list[d]):
                city1 = deg2list[b][0]
                for city2 in deg2list[d]:
                    if not adj[city1][city2]:
                        return b + d
                return b + d - 1
