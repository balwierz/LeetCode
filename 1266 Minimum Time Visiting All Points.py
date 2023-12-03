class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(x-y) for x, y in zip(a,b)) for a, b in pairwise(points))
