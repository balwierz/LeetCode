class Solution:
    def reverseVowels2(self, s: str) -> str:
        def isVowel(c):
            l = c.lower()
            return l == 'a' or l == 'i' or l == 'u' or l == 'e' or l == 'o'

        vowels = []
        for c in s:
            if isVowel(c):
                vowels.append(c)
        vowels.reverse()
        
        ret = []
        i = 0
        for c in s:
            if isVowel(c):
                ret.append(vowels[i])
                i += 1
            else:
                ret.append(c)
        return ''.join(ret)
        
    def reverseVowels(self, s: str) -> str:
        vowels = iter(c for c in s[::-1] if c.lower() in 'aeiou')
        return "".join(next(vowels) if c.lower() in 'aeiou' else c for c in s)    
