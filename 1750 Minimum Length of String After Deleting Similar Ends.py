class Solution:
    def minimumLength(self, s: str) -> int:
        (i, j) = (0, len(s)-1)
        while i<j:
            if s[i] == s[j]:
                x = s[i]
                while i < len(s) and s[i] == x:
                    i += 1
                while j >= 0 and s[j] == x:
                    j -= 1
            else:
                return j - i + 1
        return 1 if i==j else 0
