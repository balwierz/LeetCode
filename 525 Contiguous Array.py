def findMaxLength(self, nums: List[int]) -> int:
    ret = 0
    memo = {}
    for i, x in enumerate(accumulate((x+x-1 for x in nums), initial=0)):
        if x in memo:
            ret = max(ret, i - memo[x])
        else:
            memo[x] = i
    return ret
