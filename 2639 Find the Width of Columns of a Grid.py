class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(map(lambda x: len(str(x)), [grid[i][col] for i in range(len(grid))])) for col in range(len(grid[0]))]
