class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        m, n = len(mat), len(mat[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    q.append((i, j))
        dist = 0
        while q:
            dist += 1
            for i in range(len(q)):
                i, j = q.popleft()
                for k, l in ((i, j-1), (i, j+1), (i-1, j), (i+1, j)):
                    if k>=0 and k<m and l>=0 and l<n and not visited[k][l]:
                        visited[k][l] = True
                        mat[k][l] = dist
                        q.append((k, l))
        return mat

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell:
                    top = mat[i-1][j] if i else float('inf')
                    left = mat[i][j-1] if j else float('inf')
                    mat[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell := mat[i][j]:
                    bottom = mat[i+1][j] if i < m - 1 else float('inf')
                    right = mat[i][j+1] if j < n - 1 else float('inf')
                    mat[i][j] = min(cell, bottom + 1, right + 1)
        return mat
