import queue

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inEdge = [[0, i] for i in range(n)]   # number of edges coming in and id of the node
        q = queue.PriorityQueue()
        for u, v in edges:
            inEdge[v][0] += 1
        for x in inEdge:
            q.put(x)
        ret = []
        while q.qsize():
            inDeg, nodeI = q.get()
            if inDeg == 0:
                ret.append(nodeI)
            else:
                break
        return ret
