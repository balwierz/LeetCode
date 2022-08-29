import numpy as np
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        land = np.array(land)
        m, n = land.shape
        ret = []
        for i in range(m):
            for j in range(n):
                if land[i,j]:
                    j0 = j
                    while j < n and land[i,j]:
                        j += 1
                    #j -= 1
                    i1 = i
                    while i1 < m and land[i1,j-1]:
                        i1 += 1
                    #i1 -= 1
                    land[i:i1, j0:j] = 0
                    j -= 1
                    i1 -= 1
                    ret.append((i, j0, i1, j))
        return ret
