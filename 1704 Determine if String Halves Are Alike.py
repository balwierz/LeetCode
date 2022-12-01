class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1 = Counter(s[:len(s)//2])
        c2 = Counter(s[len(s)//2:])
        d1 = 0
        d2 = 0
        for c in ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']:
            d1 += c1[c]
            d2 += c2[c]
        return d1 == d2
