class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        nBad = len(c1)
        n = len(s1)
        d = defaultdict(int)
        for i in range(len(s2)):
            d[s2[i]] += 1
            if d[s2[i]] == c1[s2[i]]:
                nBad -= 1
            elif d[s2[i]] == c1[s2[i]] + 1:
                nBad += 1
            if i>=n:
                l = s2[i-n]
                d[l] -= 1
                if d[l] == c1[l]:
                    nBad -= 1
                elif d[l] == c1[l] - 1:
                    nBad += 1
            if nBad == 0:
                return True
        return False
