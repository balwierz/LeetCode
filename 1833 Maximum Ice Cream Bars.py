class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        i = 0
        while i < len(costs) and coins > 0:
            if coins >= costs[i]:
                coins -= costs[i]
                i += 1
            else:
                break
        return i
