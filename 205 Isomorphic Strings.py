class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for a, b in zip(s,t):
            if a not in mapping:
                mapping[a] = b
            elif mapping[a] != b:
                return False
        return all(x == 1 for x in Counter(mapping.values()).values())
