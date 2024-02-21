class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ret = 0
        if left == 0:
            return 0
        posStar = ceil(log2(right - left + 1))
        for pos in range(posStar, ceil(log2(right))+1):
            grpLen = pow(2, pos)
            if (c:= left // grpLen) == right // grpLen and c & 0x1: # even group, therefore all 1
                ret |= pow(2, pos)
        return ret


    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right-1
        return left & right
