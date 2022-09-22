class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i, e in enumerate(edges):
            scores[e] += i
        
        return scores.index(max(scores))
        # by hand:
        m = 0
        ret = 0
        for i, s in enumerate(scores):
            if s > m:
                ret = i
                m = s
        return ret
