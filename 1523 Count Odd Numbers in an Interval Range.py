class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high += high % 2
        low  -= low  % 2
        return (high-low) // 2
