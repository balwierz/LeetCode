class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ret = 0
        m = 0
        for d, p in sorted([[d, p] for d, p in zip(difficulty, profit)] + [[w, inf] for w in worker]):
            if p == inf:
                ret += m
            else:
                m = max(m, p)
        return ret
