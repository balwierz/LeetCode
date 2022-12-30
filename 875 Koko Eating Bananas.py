class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def numEats(k):
            return -sum((v + k - 1) // k for v in piles)
        return bisect_left(range(1, 1000000000), -h, key=numEats) + 1
