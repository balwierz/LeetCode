class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRow, nCol = len(matrix), len(matrix[0])
        n = nRow * nCol
        def getElem(i):
            row, col = divmod(i, nCol)
            return matrix[row][col]
        l, r = 0, n
        while l + 1 < r:
            m = (l+r) // 2
            if getElem(m) <= target:
                l = m
            else:
                r = m
        return getElem(l) == target
