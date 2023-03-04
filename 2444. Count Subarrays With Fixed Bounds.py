class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lasta = None
        lastz = None
        lastBad = -1
        ret = 0
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                lastBad = i
                lasta = None
                lastz = None
                continue
            if x == minK: lasta = i
            if x == maxK: lastz = i
            if lasta is not None and lastz is not None:
                ret += min(lasta, lastz) - lastBad
        return ret
