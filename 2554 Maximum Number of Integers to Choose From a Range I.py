class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ret = 0
        s = 0
        for i in range(1, n+1):
            if i not in banned:
                s += i
                if s > maxSum:
                    return ret
                ret += 1
        return ret
                
