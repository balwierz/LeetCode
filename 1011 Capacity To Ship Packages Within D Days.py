class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        n = len(w)
        def check(capacity):
            i = 0
            for d in range(days):
                s = 0
                while i < n and s + w[i] <= capacity:
                    s += w[i]
                    i += 1
                if i == n: return True
            return False

        l = max(w) - 1
        r = max(w) * (len(w) // days + 1)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r
