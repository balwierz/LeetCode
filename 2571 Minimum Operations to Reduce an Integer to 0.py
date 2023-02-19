class Solution:
    def minOperations(self, n: int) -> int:
        ret = 0
        w = list(bin(n)[2:]) + [0]
        numOnes = 0
        for i, dig in enumerate(w):
            if dig == '1':
                numOnes += 1
            else:
                if numOnes > 1 and i+1 < len(w) and w[i+1] == '1':
                    ret += 1
                else: # 00...
                    if numOnes == 1:
                        ret += 1
                    elif numOnes > 1:
                        ret += 2
                    numOnes = 0
        return ret
