class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        @cache
        def best(eventI, k):
            if k == 0 or eventI >= len(events):
                return 0
            l = eventI
            r = len(events)
            while r-l > 1:
                mid = (l+r) // 2
                if events[mid][0] <= events[eventI][1]:
                    l = mid
                else:
                    r = mid
            return max(best(eventI+1, k), events[eventI][2] + best(r, k-1))
        return best(0, k)
