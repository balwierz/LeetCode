class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        n = len(intervals)
        a, b = newInterval
        i = 0
        while i < n and intervals[i][1] < a:
            ret.append(intervals[i])
            i += 1
        if i == n:
            ret.append(newInterval)
            return ret
        start = min(a, intervals[i][0])
        while i < n and intervals[i][1] < b:
            i += 1
        if i == n or b < intervals[i][0]:
            end = b
        else:
            end = intervals[i][1]
            i += 1
        ret.append([start, end])
        while i < n:
            ret.append(intervals[i])
            i += 1
        return ret
