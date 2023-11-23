class Solution:
    def minimumSteps(self, s: str) -> int:
        num1 = 0
        ret = 0
        for x in s:
            if x == '1':
                num1 += 1
            else:
                ret += num1
        return ret
