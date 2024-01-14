class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2): return False
        c1 = Counter(w1)
        c2 = Counter(w2)
        if set(c1.keys()) != set(c2.keys()): return False
        if( sorted(c1.values()) != sorted(c2.values())): return False
        return True
    # this is much faster
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2): return False
        a = set(w1) 
        if a != set(w2): return False
        return sorted(w1.count(x) for x in a) == sorted(w2.count(x) for x in a)
