class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        data = set()
        for a, b in pairwise(s):
            data.add(a+b)
            if b+a in data:
                return True
        return False
        
