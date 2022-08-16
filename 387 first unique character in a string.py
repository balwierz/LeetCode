import numpy as np
class Solution:
    def firstUniqChar2(self, s: str) -> int:
        cnt = np.ones(128) * 2000000
        #print(cnt[1])
        for i in range(len(s)):
            c = ord(s[i])
            if cnt[c] == 2000000: cnt[c] = i+1
            else: cnt[c] = 1000000
        m = min(cnt[range(ord('a'), ord('z')+1)])
        #print(str(cnt[ord('a')]) + " " + str(cnt[ord('d')]))
        if m == 1000000:
            return -1
        else:
            return int(m)-1
    
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        cnt2 = list(filter(lambda k : k[1] == 1, cnt.items()))
        if not cnt2:
            return -1
        return min(map(lambda k: s.index(k[0]), cnt2))
   
