class Solution:
    def restoreArray(self, a: List[List[int]]) -> List[int]:
        n = len(a) + 1
        adj = defaultdict(list)
        for u, v in a:
            adj[u].append(v)
            adj[v].append(u)
        beg, end = [k for k, v in adj.items() if len(v) == 1]
        node = adj[beg][0]
        ret = [beg]
        while node != end:
            u, v = adj[node]
            if u == ret[-1]:
                u = v
            ret.append(node)
            node = u
        ret.append(end)
        return ret
