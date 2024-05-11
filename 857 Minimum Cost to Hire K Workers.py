def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    support = sorted(([w/q, i] for i, [q, w] in enumerate(zip(quality, wage))), key = lambda x: x[0])
    heap = [-quality[support[j][1]] for j in range(k) ]
    sumQual = -sum(heap)
    heapq.heapify(heap)
    ret = sumQual * support[k-1][0]
    for i in range(k, len(quality)):
        sumQual += quality[support[i][1]] + heapq.heappushpop(heap, -quality[support[i][1]])
        ret = min(ret, sumQual * support[i][0])
    return ret
