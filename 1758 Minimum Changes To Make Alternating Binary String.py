class Solution:
    def minOperations(self, s: str) -> int:
        c0 = Counter([x for i, x in enumerate(s) if i % 2 == 0])
        c1 = Counter([x for i, x in enumerate(s) if i % 2 == 1])
        return min(c0['0'] + c1['1'], c0['1'] + c1['0'])
        
    def minOperations(self, s: str) -> int:
        c = s[::2].count("0") + s[1::2].count("1")
        return min(c, len(s) - c)
