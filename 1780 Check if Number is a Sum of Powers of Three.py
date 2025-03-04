class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            n, r = divmod(n, 3)
            if r == 2:
                return False
        return True

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return n == 0 or (n % 3 < 2 and self.checkPowersOfThree(n // 3))
