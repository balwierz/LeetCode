def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    m = len(queries)
    isRemoved = [False] * n
    ret = []
    val = sum(nums)
    heap = [(x, i) for i, x in enumerate(nums)]
    heapq.heapify(heap)
    for ind, k in queries:
        if not isRemoved[ind]:
            val -= nums[ind]
            isRemoved[ind] = True
        while k and heap:
            x, i = heapq.heappop(heap)
            if not isRemoved[i]:
                val -= x
                isRemoved[i] = True
                k -= 1
        ret.append(val)
    return ret            
