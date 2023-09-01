class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * 20
        ret = [0] * (n+1)
        bc = 0
        for i in range(1, n+1):
            j = 0
            while bits[j] == 1:
                bc -= 1
                bits[j] = 0
                j += 1
            bits[j] = 1
            bc += 1
            ret[i] = bc
        return ret
