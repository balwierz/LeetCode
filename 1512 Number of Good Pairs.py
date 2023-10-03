def numIdenticalPairs(self, nums: List[int]) -> int:
    ret = 0
    c = Counter()
    for n in nums:
        ret += c[n]
        c[n] += 1
    return ret 
