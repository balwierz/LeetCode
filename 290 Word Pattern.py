class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s, s2p = {}, {}
        if len(pattern) != len(s.split()): return False
        for c, w in zip(pattern, s.split()):
            if (c in p2s and w not in s2p) or (c not in p2s and w in s2p):
                return False
            if c in p2s and w in s2p and not p2s[c] == w:
                return False
            p2s[c] = w
            s2p[w] = c
        return True
