class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]    
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        leaves = [nodeI for nodeI in range(n) if len(adj[nodeI]) <= 1]
        nSeen = len(leaves)
        q = deque(leaves)
        while nSeen < n:
            for _ in range(len(q)):
                node = q.popleft()
                for neigh in adj[node]:
                    adj[neigh].remove(node)
                    if len(adj[neigh]) == 1:
                        q.append(neigh)
                        nSeen += 1
        return list(q)
