class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ret = 0
        while mainTank >= 5:
            pumped = min(mainTank // 5, additionalTank)
            ret += 10 * (mainTank - mainTank % 5)
            mainTank %= 5
            mainTank += pumped
            additionalTank -= pumped
        ret += mainTank * 10
        return ret
