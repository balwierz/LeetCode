class Solution:
    def __init__(self):
        self.ret = []
    
    def dfs(self, n, k, last, prefix):
        if n == 0:
            self.ret.append(int(prefix))
            return
        if last - k >= 0:
            self.dfs(n-1, k, last-k, prefix + str(last-k))
        if k and last + k <= 9:
            self.dfs(n-1, k, last+k, prefix + str(last+k))
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        for i in range(1,10):
            self.dfs(n-1, k, i, str(i))
        return self.ret
        
