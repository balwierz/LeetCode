class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(b-a, 0) for a, b in pairwise([0]+target))
