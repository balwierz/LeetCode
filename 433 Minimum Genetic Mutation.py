class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        allSeq = set([start])
        for s in bank:
            allSeq.add(s)
        if end not in allSeq:
            return -1
        allSeq = list(allSeq)
        n = len(allSeq)
        
        adj = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                diff = 0
                for k in range(8):
                    diff += (allSeq[i][k] != allSeq[j][k])
                if diff == 1:
                    adj[i][j] = True
                    adj[j][i] = True
        
        q = deque()
        visited = [False] * n
        endI = 0
        for i, s in enumerate(allSeq):
            if s == start:
                visited[i] = True
                q.append(i)
            if s == end:
                endI = i
        
        ret = 0
        while len(q):
            l = len(q)
            for i in range(l):
                k = q.popleft()
                if k == endI:
                    return ret
                for a in range(n):
                    if adj[k][a] and not visited[a]:
                        visited[a] = True
                        q.append(a)
            ret += 1
        return -1
