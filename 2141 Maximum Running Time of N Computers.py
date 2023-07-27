from numpy import minimum, sum, array
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = array(batteries)
        l, r = 0, sum(batteries) // n + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if sum(minimum(batteries, mid)) // n >= mid: l = mid
            else:           r = mid
        return l
