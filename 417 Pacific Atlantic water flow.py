import numpy as np
class Solution:
    def init(self, m, n,h):
        self.m = m
        self.n = n
        self.h = h
        self.visited = np.zeros((m,n), dtype="int")  #[[0] * n] * m
        # 4-atlantic, 8-pacific
    
    def dfs(self, i,j, visMark=1):
        '''connected mark and visited mark'''
        #print(str(i) + " " + str(j) + "  " + str(visMark))
        if self.visited[i, j] & visMark:
            return
        self.visited[i, j] |= visMark
        for a, b in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if a<0 or b<0 or a>self.m-1 or b>self.n-1:
                continue
            if self.h[i][j] <= self.h[a][b] and not self.visited[a, b] & visMark:
                self.dfs(a, b, visMark)
        
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        m = len(h)
        n = len(h[0])
        self.init(m,n,h)
        ret = []
        for i in range(m):
            self.dfs(i, 0, 8)
            self.dfs(i, n-1, 4)
        for j in range(n):
            self.dfs(0, j, 8)
            self.dfs(m-1, j, 4)
        for i in range(m):
            for j in range(n):
                if self.visited[i,j] & 12 == 12:
                    ret.append((i,j))
        return ret
