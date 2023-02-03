class Solution:
    def monkeyMove(self, n: int) -> int:
        def pow2(x):
            if x == 0:
                return 1
            x2 = x // 2
            p = pow2(x2)
            return (p*p*(2 if x%2 else 1)) % 1000000007
        return (pow2(n) - 2) % 1000000007
