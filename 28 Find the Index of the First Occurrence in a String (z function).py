class Solution:
    def strStr(self, txt: str, patt: str) -> int:
        c = patt + '$' + txt
        z = [0] * len(c)
        l, r = 0, 0
        for i in range(1, len(c)):
            if i > r:
                w = 0
                j = i
                while j<len(c) and c[j] == c[w]:
                    j += 1
                    w += 1
                z[i] = w
                if w:
                    l = i
                    r = i + w - 1
            else:  # within [l,r]
                ll = z[i-l]
                if ll < r - i + 1:
                    z[i] = ll
                else:
                    j = r + 1
                    w = r - i + 1
                    while j<len(c) and c[j] == c[w]:
                        j += 1
                        w += 1
                    z[i] = w
                    r = j - 1
                    l = i
            if z[i] == len(patt):
                return i - len(patt) - 1
        return -1
