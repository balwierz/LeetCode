class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ret, data = 0, defaultdict(deque)
        for j, x in enumerate(nums):
            data[x].append(j)
            while j-data[x][0]-len(data[x]) >= k:
                data[x].popleft()
            ret = max(ret, len(data[x]))
        return ret
