class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        rMin = list(accumulate(enumerate(nums[::-1]), func=lambda d, x : x if x[1] < d[1] else d))
        rMax = list(accumulate(enumerate(nums[::-1]), func=lambda d, x : x if x[1] > d[1] else d))
        lMin = inf
        lMax = -inf
        for i, x in enumerate(nums[:len(nums)-indexDifference]):
            if x < lMin:
                lMin = x
                iMin = i
            if x > lMax:
                lMax = x
                iMax = i
            if rMax[-1-i-indexDifference][1] - lMin >= valueDifference:
                return (iMin, len(nums) -1 -rMax[-1-i-indexDifference][0])
            if lMax - rMin[-1-i-indexDifference][1] >= valueDifference:
                return (iMax, len(nums) -1 -rMin[-1-i-indexDifference][0])
        return [-1, -1]
