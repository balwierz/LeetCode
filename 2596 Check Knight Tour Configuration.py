def checkValidGrid(self, grid: List[List[int]]) -> bool:
    n = len(grid)
    arr = [None] * (n*n)
    for row in range(n):
        for col in range(n):
            arr[grid[row][col]] = (row, col)
    pos = arr[0]
    if pos != (0,0):
        return False
    for i in range(1, n*n):
        a = abs(pos[0] - arr[i][0])
        b = abs(pos[1] - arr[i][1])
        if a == 1 and b == 2 or a == 2 and b == 1:
            pos = arr[i]
        else:
            return False
    return True
