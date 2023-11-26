class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for col in range(n):
            cum = 0
            for row in range(m):
                if matrix[row][col] == 1:
                    cum += 1
                    matrix[row][col] = cum
                else:
                    cum = 0
        ret = 0
        for row in matrix:
            stretchLen = 0
            for val, count in sorted(Counter(row).items(), key = lambda e : -e[0]):
                stretchLen += count
                ret = max(ret, stretchLen * val)
        return ret
        
