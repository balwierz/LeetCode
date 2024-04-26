class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        min0, min0I = 0, None
        for row in grid:
            for i in range(len(row)):
                if i == min0I:
                    row[i] += min1
                else:
                    row[i] += min0
            min0, min1 = inf, inf
            for i, x in enumerate(row):
                if x < min0:
                    min0I = i
                    min0  = x
            for i, x in enumerate(row):
                if i != min0I and x <= min1:
                    min1  = x
        return min(row)
