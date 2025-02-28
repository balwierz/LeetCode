class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1 += "0"
        str2 += "0"
        m, n = len(str1), len(str2)
        data = [0] * m
        track = [[0] * m]
        for i in rangea(1, n):
            newdata = [0] * m
            newdata[0] = data[0]
            t = [2]
            for j in range(1, m):
                if str1[j-1] == str2[i-1]:
                    newdata[j] = data[j-1] - 1
                    t.append(1)
                elif newdata[j-1] < data[j]:
                    newdata[j] = newdata[j-1]
                    t.append(0)
                else:
                    newdata[j] = data[j]
                    t.append(2)
            data = newdata
            track.append(t)
        i, j = n-1, m-1
        ret = []
        while i or j:
            if track[i][j] == 0:
                ret.append(str1[j-1])
                j -= 1
            elif track[i][j] == 1:
                ret.append(str1[j-1])
                j -= 1
                i -= 1
            else:
                ret.append(str2[i-1])
                i -= 1
        return ''.join(ret[::-1])
