class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        pos = 0
        while True:
            if pos == len(strs[0]):
                return ret
            letter = strs[0][pos]
            for s in strs[1:]:
                if pos == len(s):
                    return ret
                if s[pos] != letter:
                    return ret
            ret += letter
            pos += 1
