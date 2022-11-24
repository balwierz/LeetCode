class Solution:  
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = ((-1,0), (1,0), (0,1), (0,-1))
        def helper(i, j, wI):
            for k in range(4):
                row = i + dirs[k][0]
                col = j + dirs[k][1]
                if row >= 0 and row < m and col >= 0 and col < n and board[row][col] == word[wI]:
                    if wI == len(word) - 1:
                        return True
                    board[row][col] = "*"
                    if helper(row, col, wI + 1):
                        return True
                    board[row][col] = word[wI]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    board[i][j] = "*"
                    if helper(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False
