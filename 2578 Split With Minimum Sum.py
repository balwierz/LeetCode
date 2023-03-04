class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted([int(x) for x in list(str(num))])
        ret = 0
        i = 1
        p = 0
        for d in digits[::-1]:
            ret += d * i
            p += 1
            if p == 2:
                p = 0
                i *= 10
        return ret
