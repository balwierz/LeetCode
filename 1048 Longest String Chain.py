def longestStrChain(self, words: List[str]) -> int:
    ret = 1
    data = defaultdict(set)
    for w in words:
        data[len(w)].add(w)
    cur = {}
    for ll in range(1, 17):
        nextCur = {}
        for b in data[ll]:
            nextCur[b] = 1
            for i in range(ll):
                hp = b[:i] + b[i+1:]
                if hp in cur:
                    nextCur[b] = max(nextCur[b], cur[hp]+1)
            ret = max(ret, nextCur[b])
        cur = nextCur
    return ret
