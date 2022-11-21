import queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        q = queue.Queue()
        q.put(entrance)
        nStep = 0
        while not q.empty():
            nStep += 1
            for _ in range(q.qsize()):
                pos = q.get()
                for dir in ((-1,0), (1,0), (0,-1), (0,1)):
                    row = pos[0] + dir[0]
                    col = pos[1] + dir[1]
                    if row < 0 or row >= m or col < 0 or col >= n:
                        continue
                    if maze[row][col] == '.':
                        if row == 0 or row == m-1 or col == 0 or col == n-1:
                            return nStep
                        maze[row][col] = '+'
                        q.put((row, col))
        return -1
