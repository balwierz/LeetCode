class State:
    def __init__(self, k, n):
        self.numNonZero = 0
        self.counts = [0] * (n+1)
        self.k = k
        self.pos = 0
    def add(self, c):
        if self.counts[c] == 0:
            self.numNonZero += 1
        self.counts[c] += 1
    def rm(self, c):
        self.counts[c] -= 1
        if self.counts[c] == 0:
            self.numNonZero -= 1
        self.pos += 1

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = State(k+1, len(nums))
        r = State(k, len(nums))
        ret = 0
        for x in nums:
            l.add(x)
            r.add(x)
            while r.numNonZero >= r.k:
                r.rm(nums[r.pos])
            while l.numNonZero >= l.k:
                l.rm(nums[l.pos])
            ret += r.pos - l.pos
        return ret

        
