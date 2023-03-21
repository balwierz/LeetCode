def findScore(self, nums: List[int]) -> int:
    n = len(nums)
    marked = [False] * n     # in not-sorted
    sss = sorted([(num, i) for i, num in enumerate(nums)])
    ret = 0
    for num, pos in sss:
        if marked[pos]: continue
        if pos: marked[pos-1] = True
        if pos < n -1: marked[pos+1] = True
        ret += num
    return ret
