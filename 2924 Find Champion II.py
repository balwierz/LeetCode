class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDeg = [0] * n
        for a, b in edges:
            inDeg[b] += 1
        ret = []
        for i, d in enumerate(inDeg):
            if d == 0:
                ret.append(i)
        return ret[0] if len(ret) == 1 else -1
