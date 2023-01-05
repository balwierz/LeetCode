class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda point : point[0])
        ret = 0
        minClose = points[0][1]
        n = len(points)
        i = 1
        # sweep from left to right:
        while i<n:
            nextOpening = points[i][0]
            if nextOpening > minClose:
                # shoot an arrow, breaking all nInSet baloons in a set of open baloons (intervals)
                ret += 1
                minClose = points[i][1]
            else:
                minClose = min(minClose, points[i][1])
            i += 1
        return ret + 1
