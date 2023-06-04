class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        def union(x, y):
            x = find(x)
            y = find(y)
            parent[x] = y
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i, j)
        
        return sum(parent[x] == x for x in range(n))
