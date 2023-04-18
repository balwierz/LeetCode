class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        neigh = [[] for _ in range(n)]
        for a, b in edges:
            neigh[a].append(b)
            neigh[b].append(a)
        
        visitCount = [0] * n
        def dfs(parent, node, target):
            visitCount[node] += 1
            if node == target:
                return True # reached target
            for v in neigh[node]:
                if v == parent:
                    continue
                if dfs(node, v, target):
                    return True
            visitCount[node] -= 1

        for a, b in trips:
            dfs(-1, a, b)
        
        @cache
        def dp(parent: int, node: int, parentHalved: bool) -> int:
            ret = 0
            if parentHalved:
                ret = price[node] * visitCount[node]
                for v in neigh[node]:
                    if v == parent:
                        continue
                    ret += dp(node, v, False)
                return ret
            else: # parent not halved, we have two options
                a = price[node] * visitCount[node]  # not halving it
                b = price[node] * visitCount[node] // 2  # halving it
                for v in neigh[node]:
                    if v == parent:
                        continue
                    a += dp(node, v, False)
                    b += dp(node, v, True)
                return min(a, b)

        return dp(-1, 0, False)
