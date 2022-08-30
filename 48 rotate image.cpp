import numpy as np
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        for row in range(n//2):
            for j in range(row, n-row-1):
                m[row][j], m[j][n-row-1], m[n-row-1][n-j-1], m[n-j-1][row] = \
                    m[n-j-1][row], m[row][j], m[j][n-row-1], m[n-row-1][n-j-1]
        
