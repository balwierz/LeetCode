class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        best, window = 0, 0
        for i in range(len(customers)):
            if grumpy[i]:
                window += customers[i]
            if i >= minute and grumpy[i-minutes]:
                window -= customers[i-minutes]
            best = max(best, window)
        return sum(c * (1-g) for c, g in zip(customers, grumpy)) + best
