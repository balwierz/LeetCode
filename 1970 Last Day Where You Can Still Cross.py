class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = [0, 1]  # left and right virtual nodes
        coord2par = [[-1] * col for _ in range(row)]
        nodeI = 1
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            x = find(x)
            y = find(y)
            if x < y:
                parent[y] = x
            else:
                parent[x] = y
        if col == 1:
            return 0
        for epoch, [x, y] in enumerate(cells):
            x -= 1
            y -= 1
            nodeI += 1
            parent.append(nodeI)
            coord2par[x][y] = nodeI
            if y == 0:
                parent[nodeI] = 0
            elif y == col-1:
                parent[nodeI] = 1
            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if 0 <= x+dx < row and 0 <= y+dy < col and coord2par[x+dx][y+dy] != -1:
                    union(coord2par[x+dx][y+dy], nodeI)
            if find(1) == 0:
                return epoch
