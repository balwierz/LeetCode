class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        f1 = Counter(basket1)
        f2 = Counter(basket2)
        minPrice = 1000000001
        for price, count in (f1+f2).items():
            if count % 2: return -1
            minPrice = min(minPrice, price)
        fxor = (f1-f2)+(f2-f1)
        #fxor = [abs()]
        prices = [val for v in sorted(fxor) for val in [v] * (fxor[v]//2)]
        ret = 0
        for i, price in enumerate(prices[:len(prices)//2]):
            if price < 2 * minPrice:
                ret += price
            else:
                ret += minPrice * 2 * (len(prices)//2 - i)
                break
        return ret
