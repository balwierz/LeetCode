def ways(self, pizza: List[str], k: int) -> int:
    m = len(pizza)
    n = len(pizza[0])
    numApples = [[0] * (n+1) for _ in range(m+1) ]
    for i in range(m)[::-1]:
        for j in range(n)[::-1]:
            numApples[i][j] = numApples[i][j+1] + numApples[i+1][j] - numApples[i+1][j+1]+ (pizza[i][j] == 'A')
    mem = defaultdict(int)
    def helper(i, j, cutsLeft):
        nonlocal numApples
        if cutsLeft == 0:
            return 1 if numApples[i][j] > 0 else 0
        nonlocal mem
        if numApples[i][j] < cutsLeft + 1:
            return 0
        if mem[(i, j, cutsLeft)]:
            return mem[(i, j, cutsLeft)]
        ret = 0
        for rCut in range(i+1, m):
            if numApples[i][j] - numApples[rCut][j]:
                ret += helper(rCut, j, cutsLeft-1)
        for cCut in range(j+1, n):
            if numApples[i][j] - numApples[i][cCut]:
                ret += helper(i, cCut, cutsLeft-1)
        ret %= 1000000007
        mem[(i, j, cutsLeft)] = ret
        return ret
    return helper(0, 0, k-1) % 1000000007
