class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # init:
        costs = [(c, i) for i, c in enumerate(costs)]
        isContiguous = len(costs) <= 2*candidates
        if isContiguous:
            h = costs.copy()
        else:
            h = costs[:candidates] + costs[len(costs)-candidates:]
        heapq.heapify(h)
        i = candidates-1  # last included
        j = len(costs)-candidates
        # loop:
        ret = 0
        for _ in range(k):
            val, ind = heapq.heappop(h)
            ret += val
            if ind <= i:
                i += 1
                if i < j:
                    heapq.heappush(h, costs[i])
            else:
                j -= 1
                if i < j:
                    heapq.heappush(h, costs[j])
        return ret
