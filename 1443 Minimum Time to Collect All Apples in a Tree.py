class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in  range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node, parent):
            retApple = hasApple[node]
            retLength = 0
            for u in adj[node]:
                if u != parent:
                    length, apple = dfs(u, node)
                    retApple |= apple
                    if apple:
                        retLength += 2 + length
            return (retLength, retApple)
        length, apple = dfs(0, -1)
        return length
