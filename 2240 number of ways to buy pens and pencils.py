class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cost2, cost1 = sorted([cost1, cost2])
        ret = 0
        for i in range(total//cost1+1):
            t = total - cost1 * i
            ret += t//cost2 + 1
        return ret
