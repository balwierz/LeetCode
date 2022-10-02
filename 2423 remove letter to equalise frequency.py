class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        m = min(c.values())
        x = max(c.values())
        t = [v for v in c.values() if v != m]
        z = [v for v in c.values() if v != x]
        if len(c) == 1:
            return True
        if m == 1 and len(z) == 1:
            return True
        if len(t) == 0 and m == 1:
            return True
        return True if len(t) == 1 and t[0] == m+1 else False
