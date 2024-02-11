def cherryPickup(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    state = [[-inf] * n for _ in range(n)]
    newState = copy.deepcopy(state)
    state[0][n-1] = grid[0][0] + grid[0][n-1]
    for row in range(1, m):
        for left in range(n-1):
            for right in range(left+1, n):
                newState[left][right] = grid[row][left] + grid[row][right] + \
                    max(state[i][j] for i in range(max(0, left-1), left+2) for j in range(max(i+1, right-1), min(right+2, n)))
        state, newState = newState, state
    return max(state[i][j] for i in range(n-1) for j in range(i+1, n))     
