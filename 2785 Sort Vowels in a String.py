class Solution:
    def sortVowels(self, s: str) -> str:
        c = Counter(s)
        vchar = "AEIOUaeiou"
        ret = ''
        i = 0
        for x in s:
            if x in vchar:
                while c[vchar[i]] == 0:
                    i += 1
                ret += vchar[i]
                c[vchar[i]] -= 1
            else:
                ret += x
        return ret
