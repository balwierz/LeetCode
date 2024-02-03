def numberOfPairs(self, points: List[List[int]]) -> int:
    n = len(points)
    byx = sorted([points[i] for i in range(n)], key=lambda x: (x[0], -x[1]))
    ret = 0
    for ic, [xc, yc] in enumerate(byx):    # chisato index, x, y
        m = -inf   # lowest value
        for [xt, yt] in byx[ic+1:]:
            if yt > m and yt <= yc:
                m = yt
                ret += 1
    return ret
