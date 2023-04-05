class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ret = 0
        what = '0'
        lens = [0,0]
        for c in s+'0':
            if c == what:
                lens[ord(c) - ord('0')] += 1
            else:
                if c == '0':
                    ret = max(ret, min(lens))
                    lens = [1,0]
                    what = '0'
                else:
                    lens[1] += 1
                    what = '1'
        return ret*2
