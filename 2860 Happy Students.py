def countWays(self, nums: List[int]) -> int:
    c = Counter(nums)
    ret = 0
    last = -1
    c[999999] = 0
    numSel = 0
    for k in sorted(c.keys()):
        if last < numSel < k:
            ret += 1
        last = k
        numSel += c[k]
    return ret
