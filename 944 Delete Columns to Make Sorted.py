class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        def isUnsorted(col):
            c = ord(strs[0][col])
            i = 1
            while(i<m and ord(strs[i][col]) >= c):
                c = ord(strs[i][col])
                i += 1
            return i!=m
        return sum(map(isUnsorted, range(n)))
