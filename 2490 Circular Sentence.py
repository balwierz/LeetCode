class Solution:
    def isCircularSentence(self, s: str) -> bool:
        v = s.split(" ")
        return v[0][0] == v[-1][-1] and all(v[i][-1] == v[i+1][0] for i in range(len(v)-1))
