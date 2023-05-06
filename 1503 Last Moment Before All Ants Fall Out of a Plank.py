class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(n-min(right) if len(right) else 0, max(left) if len(left) else 0)
