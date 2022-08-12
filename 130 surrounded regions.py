class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        stack = deque()
        for i in range(m):
            if board[i][0] == 'O': stack.append((i, 0))
            if board[i][n-1] == 'O': stack.append((i, n-1))
        for j in range(1, n-1):
            if board[0][j] == 'O': stack.append((0, j))
            if board[m-1][j] == 'O': stack.append((m-1, j))
        while(len(stack)):
            (i, j) = stack.pop()
            board[i][j] = "W"
            for a, b in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if(0 <= a < m and 0 <= b < n and board[a][b] == 'O'):
                    stack.append((a, b))
        for i in range(m):
            for j in range(n):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                elif(board[i][j] == "W"):
                    board[i][j] = "O"
