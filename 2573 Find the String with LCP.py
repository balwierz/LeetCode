class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        seq = [0] * n
        letter = ord('a')
        lcp.append([0] * (n+1))
        for i in range(0, n):
            if not seq[i]:
                for j in range(i, n):
                    if lcp[i][j]:
                        seq[j] = letter
                letter += 1
        if letter > ord('z') + 1:
            return ""
        for i in reversed(range(n)):
            for j in range(i+1):
                if not (lcp[i][j] == lcp[j][i] == (lcp[i+1][j+1] + 1 if seq[i] == seq[j] else 0)):
                    return ""
        return ''.join([chr(i) for i in seq])
