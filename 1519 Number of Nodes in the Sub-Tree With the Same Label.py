class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans = [10] * n
        def dfs(node, parent):
            ret = [0] * 26
            ret[ord(labels[node]) - 97] = 1
            for u in adj[node]:
                if u != parent:
                    tmp = dfs(u, node)
                    for i in range(26):
                        ret[i] += tmp[i]
            ans[node] = ret[ord(labels[node]) - 97]
            return ret
        dfs(0, -1)
        return ans
