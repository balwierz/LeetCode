class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(max(col) for col in zip(*[sorted(x) for x in grid]))
