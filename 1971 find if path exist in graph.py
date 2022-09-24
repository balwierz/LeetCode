def find(a, parent):
    while(parent[a] != a):
        a = parent[a]
    return a

def union(a, b, parent, rank):
    a = find(a, parent)
    b = find(b, parent)
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # implement via union-find
        rank = [0] * n
        parent = [0] * n
        for i in (range(n)):
            parent[i] = i
        for u, v in edges:
            union(u, v, parent, rank)
            if find(source, parent) == find(destination, parent):
                return True
        return find(source, parent) == find(destination, parent)
