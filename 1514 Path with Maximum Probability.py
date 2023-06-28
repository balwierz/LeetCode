class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        neigh = [[] for _ in range(n)]
        for i in range(len(edges)):
            neigh[edges[i][0]].append((-log(succProb[i]), edges[i][1]))
            neigh[edges[i][1]].append((-log(succProb[i]), edges[i][0]))
        visited = [False] * n
        h = [(0, start)]
        while h:
            d, node = heapq.heappop(h)
            if node == end:
                return exp(-d)
            if visited[node]:
                continue
            visited[node] = True
            for e, nn in neigh[node]:
                heapq.heappush(h, (d+e, nn))
        return 0
