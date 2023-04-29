class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        n = len(strs)
        p = len(strs[0])

        # union find
        parent = [i for i in range(n)]
        ret = n
        def root(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = root(a), root(b)
            if a != b:
                parent[a] = b
                nonlocal ret
                ret -= 1
        
        for a in range(1, n):
            for b in range(a):
                if root(a) != root(b):
                    dist = 0
                    for i in range(p):
                        dist += int(strs[a][i] != strs[b][i])
                        if dist > 2:
                            break
                    if dist <= 2: 
                        union(a, b)

        return ret
            
