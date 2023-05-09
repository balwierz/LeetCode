class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direction = 0  # right, 1 down, 2 left, 3 up
        stepVert = m-1
        stepHori = n
        ret = []
        col = -1
        row = 0
        while(stepVert >= 0 and stepHori >= 0):
            if direction == 0:
                for j in range(col+1, col+stepHori+1):
                    ret.append(matrix[row][j])
                col += stepHori
                stepHori -= 1
                direction = 1
            elif direction == 1:
                for i in range(row+1, row+stepVert+1):
                    ret.append(matrix[i][col])
                row += stepVert
                stepVert -= 1
                direction = 2
            elif direction == 2:
                for j in range(col-1, col-stepHori-1, -1):
                    ret.append(matrix[row][j])
                col -= stepHori
                stepHori -= 1
                direction = 3
            elif direction == 3:
                for i in range(row-1, row-stepVert-1, -1):
                    ret.append(matrix[i][col])
                row -= stepVert
                stepVert -= 1
                direction = 0
                #col += 1
        return ret
