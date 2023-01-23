class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustsSomeone = [False for _ in range(n+1)]
        trustedBy = [0 for _ in range(n+1)]
        for a, b in trust:
            trustedBy[b] += 1
            trustsSomeone[a] = True
        for i in range(1, n+1):
            if trustedBy[i] == n-1 and not trustsSomeone[i]:
                return i
        return -1
