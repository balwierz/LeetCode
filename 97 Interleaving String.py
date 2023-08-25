def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    state = set([(0, 0)])
    m, n = len(s1), len(s2)
    for letter in s3:
        newState = set()
        for i, j in state:
            if i < m and s1[i] == letter:
                newState.add((i+1, j))
            if j < n and s2[j] == letter:
                newState.add((i, j+1))
        state = newState
    return (m, n) in state    
