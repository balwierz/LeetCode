class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.out = [[] for _ in range(n)]
        self.n = n
        for a, b, v in edges:
            self.out[a].append((b, v))
        
    def addEdge(self, edge: List[int]) -> None:
        self.out[edge[0]].append((edge[1], edge[2]))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        col = [0] * self.n
        heap = [(0, node1)]
        while heap:
            dist, node = heapq.heappop(heap)
            if col[node] == 2:
                continue
            if node == node2:
                return dist
            col[node] = 2
            for neigh, val in self.out[node]:
                if col[neigh] != 2:
                    heapq.heappush(heap, (dist+val, neigh))
        return -1
