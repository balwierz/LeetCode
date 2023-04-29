class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # add index to queries:
        queries = [(d, a, b, ind) for ind, (a, b, d) in enumerate(queries)]
        # sort by distance cutoff:
        queries.sort(key = lambda x: x[0])
        # sort edges by distance:
        edges.sort(key = lambda x: x[2])
        edgeI = 0
        parent = [i for i in range(n)]
        def root(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            x = root(x)
            y = root(y)
            parent[x] = y
        ret = [False for _ in range(len(queries))]
        for queryDist, a, b, ind in queries:
            # first union all edges with distance < queryDist
            while edgeI < len(edges) and edges[edgeI][2] < queryDist:
                union(edges[edgeI][0], edges[edgeI][1])
                edgeI += 1
            ret[ind] = (root(a) == root(b))
        return ret
