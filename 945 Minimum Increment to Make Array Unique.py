class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        drag = 0
        ret = 0
        for a, b in pairwise(chain(sorted(nums), [999999999])):
            if a == b:
                drag += 1
            else:
                toFill = b - a - 1
                m = min(drag, toFill)
                ret += m * (m+1) // 2
                drag -= m
                ret += drag * (b-a)
        return ret
