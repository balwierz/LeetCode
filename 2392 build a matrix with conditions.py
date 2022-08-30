import numpy as np

class NotADag(Exception):
    pass

class Solution:
    def __init__(self):
        outEdge = {}
        visited = []
        ret = []
        
    def topoSort(self, cond, k):
        # turn into a dependency graph
        #inEdge = {} # dict of sets
        self.outEdge = {}
        self.ret = []
        self.visited = [0] * (k+1)
        for sm, gt in cond:
            try:
                self.outEdge[sm].add(gt)
            except KeyError:
                self.outEdge[sm] = set((gt,))
        for v in range(1, k+1):
            self.helper(v)  # modifies ret
        self.ret.reverse()
        return self.ret
    
    def helper(self, v):
        if self.visited[v] == 2:
            return
        if self.visited[v] == 1:
            raise NotADag
        self.visited[v] = 1
        try:
            for node in self.outEdge[v]:
                self.helper(node)
        except KeyError:
            pass
        self.visited[v] = 2
        self.ret.append(v)
        return
        
    def buildMatrix(self, k: int, rowC: List[List[int]], colC: List[List[int]]) -> List[List[int]]:
        try:
            rt = np.array(self.topoSort(rowC, k), dtype="int")
            ct = np.array(self.topoSort(colC, k), dtype="int")
        except NotADag:
            return []
        ret = np.zeros((k, k), dtype="int")
        ret[np.argsort(rt-1), np.argsort(ct-1)] = range(1, k+1)
        return ret.tolist()
