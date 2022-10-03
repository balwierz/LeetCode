class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = colors + 'X'
        neededTime = neededTime + [0]
        lastCol = ' '
        rSum = 0
        thisMax = 0
        ret = 0
        #thisLen = 0
        for c, t in zip(colors, neededTime):
            if c != lastCol:
                ret += rSum - thisMax
                thisMax = t
                rSum = t
                lastCol = c
            else:
                rSum += t
                thisMax = max(thisMax, t)
        return ret
