def islandPerimeter(self, grid: List[List[int]]) -> int:
    return sum(a != b for v in chain(grid, zip(*grid)) for a, b in pairwise(v)) + sum(grid[0]) + sum(grid[-1]) + sum(grid[i][0] + grid[i][-1] for i in range(len(grid)))
