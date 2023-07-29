class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        @cache
        def solve(A, B):
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1.0
            if B <= 0:
                return 0.0
            return 0.25 * (solve(A-100, B) + solve(A-75, B-25) + solve(A-50, B-50) + solve(A-25, B-75))
        return solve(n, n)
