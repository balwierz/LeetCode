class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        cost = [[inf] * (len(s2)+1) for _ in range(len(s1)+1)]
        cost[-1][-1] = 0
        s = 0
        for i in range(len(s1)):
            s += ord(s1[i])
            cost[i][-1] = s
        s = 0
        for i in range(len(s2)):
            s += ord(s2[i])
            cost[-1][i] = s
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    cost[i][j] = cost[i-1][j-1]
                cost[i][j] = min(cost[i][j], cost[i-1][j] + ord(s1[i]), cost[i][j-1] + ord(s2[j]))
        return cost[len(s1)-1][len(s2)-1]
