class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ret = []
        path = [0]
        def backtrack(node):
            nonlocal path
            if node == n-1:
                ret.append(path.copy())
                return;
            for v in graph[node]:
                path.append(v)
                backtrack(v)
                path.pop()
            return
        backtrack(0)
        return ret
