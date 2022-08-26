class Solution:
    def __init__(self):
        self.len2counters = [[] for i in range(10)]
        n = 1
        while(n<=1000000000):
            s = str(n)
            self.len2counters[len(s)].append(Counter(s))
            n *= 2
            
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        l = len(s)
        cs = Counter(s)
        for i in range(len(self.len2counters[l])):
            if self.len2counters[l][i] == cs:
                return True
        return False
