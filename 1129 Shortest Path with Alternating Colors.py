from queue import SimpleQueue
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redOut = [[] for _ in range(n)]
        bluOut = deepcopy(redOut)
        for a, b in redEdges:  redOut[a].append(b)
        for a, b in blueEdges: bluOut[a].append(b)
        
        visitedR, visitedB = [False] * n, [False] * n
        visitedR[0] = True
        visitedB[0] = True
        ret = [-1] * n
        p, q = SimpleQueue(), SimpleQueue()
        p.put([0, 'r'])
        p.put([0, 'b'])
        step = 0
        while p.qsize():
            while p.qsize():
                node, inCol = p.get()
                if inCol == 'r':
                    out = bluOut[node]
                    outCol = 'b'
                    visited = visitedB
                else:
                    out = redOut[node]
                    outCol = 'r'
                    visited = visitedR
                if ret[node] == -1:
                    ret[node] = step
                for u in out:
                    if not visited[u]:
                        q.put([u, outCol])
                        visited[u] = True
            p = q
            q = SimpleQueue()
            step += 1
        return ret
