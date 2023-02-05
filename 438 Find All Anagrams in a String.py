class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        nBad = len(c)
        d = defaultdict(int)
        ret = []
        for i, l in enumerate(s):
            if d[l] == c[l]:
                nBad += 1
            d[l] += 1
            if d[l] == c[l]:
                nBad -= 1
            if i >= len(p):
                k = s[i-len(p)]
                if d[k] == c[k]:
                    nBad += 1
                d[k] -= 1
                if d[k] == c[k]:
                    nBad -= 1
            if nBad == 0:
                ret.append(i-len(p)+1)
        return ret
        
