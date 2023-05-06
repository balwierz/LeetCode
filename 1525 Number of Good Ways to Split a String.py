class Solution:
    def numSplits0(self, s: str) -> int:
        ret = 0
        left = set()
        right = Counter(s)
        nLeft = 0
        nRight = len(right.keys())
        for x in s:
            if x not in left:
                nLeft += 1
                left.add(x)
            right[x] -= 1
            if right[x] == 0:
                nRight -= 1
            if nLeft == nRight:
                ret += 1
            elif nLeft > nRight:
                break
        return ret

    def numSplits(self, s: str) -> int:
        first, last = {}, {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        ranges = sorted([*first.values(), *last.values()])
        M = len(ranges) // 2
        return ranges[M] - ranges[M - 1]
