class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        nRow = len(grid)
        nCol = len(grid[0])
        for i in range(nRow):
            grid[i] = [1] + grid[i] + [-1]
        ret = [0] * nCol
        for b in range(nCol):
            pos = b+1
            for r in range(nRow):
                if grid[r][pos] == 1:
                    if grid[r][pos+1] == -1:
                        pos = 0
                        break
                    else:
                        pos += 1
                else:
                    if grid[r][pos-1] == 1:
                        pos = 0
                        break
                    else:
                        pos -= 1
            ret[b] = pos - 1
        return ret
