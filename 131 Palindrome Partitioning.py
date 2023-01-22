class Solution:
    def __init__(self):
        self.memo = [None for _ in range(20)]

    def partition(self, s: str, k=0 ) -> List[List[str]]:
        #def isPal(s: str) -> bool:
        #    for i in range(len(s)//2):
        #        if s[i] != s[len(s)-1-i]:
        #            return False
        #    return True
        
        if len(s) == 0:
            return [[]]
        if self.memo[k]:
            return self.memo[k]
        ret = []
        for i in range(len(s)):
            ss = s[:(i+1)]
            if ss == ss[::-1]: #isPal(s[:(i+1)]):
                for sol in self.partition(s[(i+1):], len(s)-i) :
                    ret.append([ s[:(i+1)] ] + sol )
        self.memo[k] = ret
        return ret
