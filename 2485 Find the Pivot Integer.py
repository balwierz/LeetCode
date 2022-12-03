class Solution:
    def pivotInteger(self, n: int) -> int:
        ret = sqrt(n*(n+1)//2)
        if int(ret) == ret:
            return int(ret)
        return -1
