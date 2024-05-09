class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(max(0, x-i) for i, x in enumerate(heapq.nlargest(k, happiness)))
