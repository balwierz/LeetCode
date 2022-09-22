class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        free = 0
        sets = Counter()
        for row in matrix:
            needed = frozenset(i for i in range(len(row)) if row[i])
            if not needed:
                free += 1
                continue
            sets[needed] += 1
        best = 0
        for c in combinations(range(len(matrix[0])), r=numSelect):
            cur = 0
            c = frozenset(c)
            for x, amt in sets.items():
                if x.issubset(c):
                    cur += amt
            best = max(best, cur)
        return best + free

class Solution2:
    def maximumRows(self, mat: List[List[int]], numSelect: int) -> int:
        m = len(mat)
        n = len(mat[0])
        row2cols = [[] for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row2cols[i].append(j)
        marked = [False] * n
        
        def checkRows():
            ret = 0
            for row in range(m):
                covered = True
                for col in row2cols[row]:
                    if not marked[col]:
                        covered = False
                        break
                if covered:
                    ret += 1
            return ret
            
        def dfs(minCol, leftSelect):
            #print("dfs mincol=" + str(minCol) + " leftSelect=" + str(leftSelect))
            if leftSelect == 0:
                return checkRows()
            if n - minCol < leftSelect:
                return 0
            a = dfs(minCol+1, leftSelect)   # we dont mark the leftSelect column
            marked[minCol] = True
            b = dfs(minCol+1, leftSelect-1)
            marked[minCol] = False
            return max(a, b)
        
        return dfs(0, numSelect)
        
