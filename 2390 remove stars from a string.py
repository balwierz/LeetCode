class Solution:
    def removeStars(self, s: str) -> str:
        cnt = 0
        s = list(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                cnt += 1
                s[i] = ''
            elif cnt:
                s[i] = ''
                cnt -= 1
        return ''.join(s)
            
