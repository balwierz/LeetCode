import bisect
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price = sorted(price)
        def isImpossible(priceDelta):
            largest = price[0]
            largestI = 0
            for i in range(1, k):
                j = largestI
                while j < len(price) and price[j] < largest + priceDelta:
                    j += 1
                if j == len(price):
                    return True
                largestI = j
                largest = price[j]
            return False
        return bisect_left(range(int(price[-1]/(k-1))+1), True, key=isImpossible) - 1
