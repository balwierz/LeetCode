import numpy as np
#from pipe import *
def process(mat):
    m = len(mat)
    return [[max(row[j:j+3]) for j in range(m-2)] for row in mat]

def process2(mat):
    m = len(mat)
    return [[max(mat[i:i+3, j]) for j in range(m-2)] for i in range(m-2)]

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ret = process(grid)
        ret = process2(np.array(ret))
        return ret
        
