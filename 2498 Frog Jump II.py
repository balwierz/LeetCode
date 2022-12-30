class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ret = 0
        n = len(stones)
        if n == 2:
            return stones[1] - stones[0]
        if n == 3:
            return stones[2] - stones[0]
        ret = max([stones[i] - stones[i-2] for i in range(2,n,2)])
        ret = max(ret, max([stones[i] - stones[i-2] for i in range(3,n,2)]))
        return ret
