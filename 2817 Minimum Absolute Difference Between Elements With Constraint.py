from sortedcontainers import SortedSet

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        data = SortedSet()
        ret = inf
        for i, num in enumerate(nums[x:]):
            data.add(nums[i])
            l = data.bisect(num)
            if l > 0:
                ret = min(ret, num - data[l-1])
            if l < len(data):
                ret = min(ret, data[l] - num)
        return ret
