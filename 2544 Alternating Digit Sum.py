class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        w = '+'.join(s[0::2]) + "-(" + '+'.join(s[1::2]) + "+0)"
        return eval(w)
