class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)
        numNeg = 0
        ret = ""
        for c in t:
            cnt[c] -= 1
        # cnt contains negative numbers; a window is valid if \all cnt[c] >= 0
        for c in cnt:
            numNeg += 1        
        j = 0
        for i, c in enumerate(s):
            cnt[c] += 1
            if cnt[c] == 0:
                numNeg -= 1
            while numNeg == 0:    # we just reached a valid window, let's shorten
                cnt[s[j]] -= 1
                if cnt[s[j]] < 0:  # we just shortened the window too much
                    numNeg += 1
                    if i-j+1 < len(ret) or ret == "":
                        ret = s[j:i+1]
                j += 1
        return ret
