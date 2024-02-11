def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    colMax = [max(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0]))]
    return [[matrix[row][col] if matrix[row][col] != -1 else colMax[col] for col in range(len(matrix[0]))] for row in range(len(matrix))]
