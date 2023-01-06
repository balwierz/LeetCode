class Solution:
    def countDigits(self, num: int) -> int:
        return sum(map(lambda d : num % int(d) == 0, str(num)))
