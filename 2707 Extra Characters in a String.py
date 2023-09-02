class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def findall(p, s):
            i = s.find(p)
            while i != -1:
                yield i
                i = s.find(p, i+1)
        allPos = [ (pos, pos+len(w)) for w in dictionary for pos in findall(w, s) ] 
        ends = [[] for _ in range(len(s)+1)]
        for a, b in allPos:
            ends[b].append(a)
        dp = [0] + [inf] * len(s)
        for e in range(1, len(s) + 1):
            dp[e] = dp[e-1] + 1
            for beg in ends[e]:
                dp[e] = min(dp[e], dp[beg])
        return dp[-1]
