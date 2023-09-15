class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) for j in range(len(points)) for i in range(len(points))]
        heapq.heapify(dist)
        parent = [i for i in range(len(points))]
        ret = 0
        def root(x):
            while parent[x] != x:
                parent[x] =parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            a = root(a)
            b = root(b)
            parent[a] = b
        numComponents = len(points)
        while numComponents != 1:
            d, a, b = heapq.heappop(dist)
            if root(a) != root(b):
                numComponents -= 1
                union(a, b)
                ret += d
        return ret
