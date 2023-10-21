from sortedcontainers import *
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        ret = -inf
        candidates = SortedSet([(0, -1),])
        x2val = []
        for i, x in enumerate(nums):
            if i > k:
                candidates.remove((x2val[i-k-1], i-k-1))
            best = candidates[-1][0] + x
            ret = max(ret, best)
            candidates.add((best, i))
            x2val.append(best)
        return ret
        
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        for i in range(len(nums)):
            if q: nums[i] += q[0]
            while q and q[-1] < nums[i]: q.pop()
            if nums[i] > 0: q.append(nums[i])
            if q and i>=k and q[0] == nums[i-k]:
                q.popleft()
        return max(nums)
