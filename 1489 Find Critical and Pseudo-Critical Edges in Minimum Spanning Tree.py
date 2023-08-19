class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = size
    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def join(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a != b:
            self.parent[b] = a
            self.size -= 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted([(a, b, v, i) for i, [a, b, v] in enumerate(edges)], key=lambda e: e[2])
        def tryEdge(eI, dsu = DSU(n), score=0):
            for i, [a, b, v, ind] in enumerate(edges):
                if i == eI:
                    continue
                if dsu.root(a) != dsu.root(b):
                    dsu.join(a, b)
                    score += v
                    if dsu.size == 1:
                        break
            return inf if dsu.size > 1 else score
        minScore = 0
        candidates = set()
        dsu = DSU(n)
        for i, [a, b, v, ind] in enumerate(edges):
            if dsu.root(a) != dsu.root(b):
                dsu.join(a, b)
                minScore += v
                candidates.add(i)
                if dsu.size == 1:
                    break
        if dsu.size > 1:   #not possible to build a tree
            return [[],[]]
        critical, pseudocritical = [], []

        for i in candidates:
            score = tryEdge(i, DSU(n))
            if score == minScore:
                pseudocritical.append(edges[i][3])
            else:
                critical.append(edges[i][3])
        for i, [a, b, v, ind] in enumerate(edges):
            if i in candidates:
                continue
            dsu = DSU(n)
            dsu.join(a, b)
            if tryEdge(-1, dsu, v) == minScore:
                pseudocritical.append(edges[i][3])
        return [critical, pseudocritical]
