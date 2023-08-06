class Solution:
    def finalString(self, s: str) -> str:
        ret = ''
        for txt in s.split('i'):
            ret = ret[::-1] + txt
        return ret
