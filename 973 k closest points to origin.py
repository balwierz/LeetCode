import queue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = map(lambda p: p[0]*p[0]+p[1]*p[1], points)
        q = queue.PriorityQueue()
        for e in zip(dists, points):
            q.put(e)
        return [q.get()[1] for _ in range(k)]
        
