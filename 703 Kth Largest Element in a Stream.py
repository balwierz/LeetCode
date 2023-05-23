class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = nums[:k]
        heapify(self.q)
        for a in nums[k:]:
            if a > self.q[0]:
                heappop(self.q)
                heappush(self.q, a)
        
    def add(self, val: int) -> int:
        if len(self.q) == self.k:
            if val > self.q[0]:
                heappop(self.q)
                heappush(self.q, val)
        else:
            heappush(self.q, val)
        return self.q[0]
        
