from sortedcontainers import SortedList, SortedSet, SortedDict
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        seen, ret = SortedList(), 0
        for v in nums:
            ret += seen.bisect_right(upper-v) - seen.bisect_left(lower-v)
            seen.add(v)
        return ret
