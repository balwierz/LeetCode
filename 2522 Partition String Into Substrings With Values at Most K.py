class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ret = 0
        i = 0
        j = 1
        n = len(s)
        while j<=n:
            if k < int(s[i:j]):
                if j == i + 1:
                    return -1
                ret += 1
                i = j-1
            else:
                j += 1
        return ret + 1
