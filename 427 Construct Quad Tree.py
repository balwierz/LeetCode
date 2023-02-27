def construct(self, grid: List[List[int]]) -> 'Node':
    def helper(r0, r1, c0, c1):
        if r0 + 1 == r1:
            return [Node(grid[r0][c0], True, None, None, None, None), grid[r0][c0]]
        n0, v0 = helper(r0, (r0+r1)//2, c0, (c0+c1)//2)
        n1, v1 = helper(r0, (r0+r1)//2, (c0+c1)//2, c1)
        n2, v2 = helper((r0+r1)//2, r1, c0, (c0+c1)//2)
        n3, v3 = helper((r0+r1)//2, r1, (c0+c1)//2, c1)
        if v0+v1+v2+v3 == 0:
            return [Node(0, True, None, None, None, None), 0]
        elif v0+v1+v2+v3 == 4:
            return [Node(1, True, None, None, None, None), 1]
        else:
            return [Node(0, False, n0, n1, n2, n3), 0.5]
    return helper(0, len(grid), 0, len(grid))[0]
