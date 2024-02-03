def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    n = len(arr)
    @cache
    def helper(i):
        if n-i <= k:
            return max(arr[i:]) * (n-i)
        val = 0
        ret = 0
        for end in range(i+1, i+k+1):
            val = max(val, arr[end-1])
            ret = max(ret, val*(end - i) + helper(end))
        return ret
    return helper(0)        
