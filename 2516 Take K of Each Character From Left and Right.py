class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        count = defaultdict(int)
        numBad = 3
        i = -1
        while i>=-len(s) and numBad != 0:
            count[s[i]] += 1
            if count[s[i]] == k:
                numBad -= 1
            i -= 1
        i += 1
        if numBad:
            return -1
        ret = - i
        j = 0
        while i<=0 and j < len(s):
            if count[s[i]] == k:
                numBad += 1
            count[s[i]] -= 1
            i += 1
            while j < len(s) and numBad:
                count[s[j]] += 1
                if count[s[j]] == k:
                    numBad -= 1
                j += 1
            if i <= 0:
                ret = min(ret, j-i)
        return ret
