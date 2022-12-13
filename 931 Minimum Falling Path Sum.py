class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1: return matrix[0][0]
        for row in range(1, n):
            matrix[row][0] += min(matrix[row-1][0], matrix[row-1][1])
            matrix[row][n-1] += min(matrix[row-1][n-2], matrix[row-1][n-1])
            for col in range(1, n-1):
                matrix[row][col] += min(matrix[row-1][col-1], matrix[row-1][col], matrix[row-1][col+1])
        return min(matrix[n-1])
