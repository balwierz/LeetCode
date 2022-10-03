class LUPrefix:
    parent : List[int]
    n : int
    def __init__(self, n: int):
        self.parent = [-1] * (n+1)
        self.n = n

    def upload(self, v: int) -> None:
        self.parent[v] = v
        if v != 0 and self.parent[v-1] != -1:
            self.union(v-1, v)
        if v != self.n and self.parent[v+1] != -1:
            self.union(v, v+1)

    def root(self, v : int) -> int:
        if v == -1:
            return -1
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v
            
    def union(self, i : int, j: int) -> None:
        if i < j:
            self.parent[i] = self.root(j)
        else:
            self.parent[j] = self.root(i)
        
    def longest(self) -> int:
        if self.parent[1] == -1:
            return 0
        return self.root(1)
