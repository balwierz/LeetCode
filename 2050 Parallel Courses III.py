class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        inDeg = [0] * n
        out = [[] for _ in range(n)]
        for a, b in relations:
            inDeg[b-1] += 1
            out[a-1].append(b-1)
        jobs = []
        for i, x in enumerate(inDeg):
            if x == 0:
                heapq.heappush(jobs, (time[i], i))
        clock = 0
        while(jobs):
            clock, x = heapq.heappop(jobs)
            for y in out[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    heapq.heappush(jobs, (clock+time[y], y))
        return clock
