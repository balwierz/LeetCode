class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        dig = [0] * 64
        for i in range(10):
            dig[ord('0') + i] = i
        ret = [0] * n
        x = 0
        for i, d in enumerate(word):
            x = (10 * x + dig[ord(d)]) % m
            if not x:
                ret[i] = 1
        return ret
