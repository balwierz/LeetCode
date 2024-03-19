class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        heap = [-x for x in Counter(tasks).values()]
        heapq.heapify(heap)
        w = n+1
        q = [None] * w
        i = 0
        while heap:
            x = q[i%w] 
            if x:
                heapq.heappush(heap, x)
                q[i%w] = None
            y = heapq.heappop(heap) + 1
            if y:
                q[i%w] = y
            i += 1
        # now the heap will be empty and we can stop simulation and calculate how many iterations more
        # The heap is empty. We need to get the time coordinate of the last element
        m = max([-x for x in q if x], default = 0)
        if m:
            for j in range(-1, -w-1, -1):
                if q[(i+j)%w] == -m:
                    i += m * w + j + 1
                    break
        return i

    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks).values()
        m = max(c)
        return max(len(tasks), (n+1)*(m-1) + sum(x == m for x in c))
