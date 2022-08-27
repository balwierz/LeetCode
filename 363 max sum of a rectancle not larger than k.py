# this solution is too slow to pass the tests
class Solution:
    def __init__(self):
        cs = []
    def getCumSum(self, nums):
        m = len(nums)
        n = len(nums[0])
        self.cs = [[] for i in range(m+1)]
        for i in range(m+1):
            self.cs[i] = [0 for j in range(n+1)] 
        
        for i in range(m):
            for j in range(n):
                self.cs[i][j] = nums[i][j] + self.cs[i][j-1] + self.cs[i-1][j] - self.cs[i-1][j-1]
                #print("".join([str(x) for x in (i, j, self.cs[i][j])]))
   
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def field(i0, j0, i1, j1):  # sum of a rectangle
            ret = self.cs[i1][j1] + self.cs[i0-1][j0-1] - self.cs[i1][j0-1] - self.cs[i0-1][j1]
            #print(" ".join([str(x) for x in (i0, j0, i1, j1, ret)]))
            return ret
        self.getCumSum(matrix)
        
        bestRet = -1000000001
        for i0 in range(m):
            for j0 in range(n):
                h = self.cs[i0-1][j0-1]
                for i1 in range(i0, m):
                    g = -self.cs[i1][j0-1]
                    for j1 in range(j0, n):
                        #f = field(i0, j0, i1, j1)
                        f = h + g + self.cs[i1][j1] - self.cs[i0-1][j1]
                        if f <= k and f > bestRet:
                            bestRet = f
        return bestRet
