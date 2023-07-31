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


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = [ord(x) for x in s1]
        s2 = [ord(x) for x in s2]
        cost = [inf] * (len(s2)+1)
        cost[-1] = 0
        s = 0
        for i in range(len(s2)):
            s += s2[i]
            cost[i] = s
        for i in range(len(s1)):
            last = cost[-1]
            cost[-1] += s1[i]
            for j in range(len(s2)):
                tmp = cost[j]
                cost[j] = inf
                if s1[i] == s2[j]:
                    cost[j] = last
                cost[j] = min(cost[j], tmp + s1[i], cost[j-1] + s2[j])
                last = tmp
        return cost[len(s2)-1]
