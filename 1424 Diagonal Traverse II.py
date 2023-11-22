def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    return [x for a,b,x in sorted([(rowI+colI, colI, x) for rowI, row in enumerate(nums) for colI, x in enumerate(row)])]
