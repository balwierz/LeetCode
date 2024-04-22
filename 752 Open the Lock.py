class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        cube = [[[[0] * 10 for a in range(10)] for b in range(10)] for c in range(10)]
        for deadEnd in deadends:
            (i, j, k, l) = map(int, deadEnd)
            cube [i][j][k][l] = 1
        target = list(map(int, target))
        if all(x==0 for x in target):
            return 0
        q = deque([target])
        step = 0
        while q:
            n = len(q)
            while n:
                pos = q.popleft()
                for dim in range(4):
                    for fwd in [-1, 2]:
                        pos[dim] = (pos[dim] + fwd) % 10
                        if cube[pos[0]][pos[1]][pos[2]][pos[3]] == 0:
                            cube[pos[0]][pos[1]][pos[2]][pos[3]] = 1
                            if all(x==0 for x in pos):
                                return step + 1
                            q.append(pos.copy())
                    pos[dim] = (pos[dim] - 1) % 10
                n -= 1
            step += 1
        return -1
        
