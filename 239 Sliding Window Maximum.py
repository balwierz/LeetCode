import sortedcontainers
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []
        for i, num in enumerate(nums):
            while len(q) and num >= q[-1][0]:
                q.pop()
            q.append((num, i))
            if i >= k-1:
                ret.append(q[0][0])
                if i-k+1 == q[0][1]:
                    q.popleft()
        return ret


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = sortedcontainers.SortedDict()
        ret = []
        for num in nums[:k-1]:
            d[num] = d.setdefault(num, 0) + 1
        for i, num in enumerate(nums[k-1:]):
            d[num] = d.setdefault(num, 0) + 1
            ret.append(d.peekitem()[0])
            if d[nums[i]] == 1:
                del d[nums[i]]
            else:
                d[nums[i]] -= 1
        return ret
