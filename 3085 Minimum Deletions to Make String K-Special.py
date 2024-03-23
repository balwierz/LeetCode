def minimumDeletions(self, word: str, k: int) -> int:
    z, ret = 0, inf
    for v, b in pairwise([0] + (c := sorted(Counter(word).values()))):
        z += v
        ret = min(ret, z + sum(x - (b+k) if x > b+k else 0 for x in c))
    return ret
