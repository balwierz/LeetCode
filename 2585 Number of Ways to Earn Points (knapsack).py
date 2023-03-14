class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        prev = [0] * (target+1)
        prev[0] = 1
        for count, points in types:
            this = prev.copy() # points used zero times
            for shift in range(points, points*count+1, points):
                if shift > target: break
                for i in range(shift, target+1):
                    this[i] += prev[i-shift]
                    this[i] %= 1000000007
            prev = this
        return this[target]
