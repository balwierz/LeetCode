class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = defaultdict(int)
        i = 0
        ret = 0
        for j, char in enumerate(s):
            c[char] += 1
            if c[char] == 1:
                ret = max(ret, j-i+1)
            else:
                while s[i] != char:
                    c[s[i]] = 0
                    i += 1
                c[char] = 1
                i += 1
        return ret
