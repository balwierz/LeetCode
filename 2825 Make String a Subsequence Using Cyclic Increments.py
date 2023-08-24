class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2): return False
        i = 0
        nextLetter = {chr(l) : chr(l+1) for l in range(ord('a'), ord('z'))}
        nextLetter['z'] = 'a'
        for letter in str2:
            while i<len(str1) and str1[i] != letter and nextLetter[str1[i]] != letter:
                i += 1
            if i == len(str1):
                return False
            i +=1
        return True
