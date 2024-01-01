class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for j, child in enumerate(g):
            while i < len(s) and s[i] < child:
                i += 1
            if i == len(s):
                return(j)
            i += 1
        return j+1
