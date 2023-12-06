class Solution:
    def totalMoney(self, n: int) -> int:
        a, b = divmod(n, 7)
        return 28 * a + 7 * (a-1) * a // 2 + b * a + (b+1) * b // 2
