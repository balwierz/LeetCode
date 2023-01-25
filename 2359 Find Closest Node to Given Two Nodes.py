class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1
        n = len(edges)
        distA = [-1] * n
        distA[node1] = 0
        distB = [-1] * n
        distB[node2] = 0
        i = node1
        j = node2
        k = 0
        while True:
            ret = []
            a = b = False
            if edges[i] != -1 and distA[edges[i]] == -1:
                i = edges[i]
                distA[i] = k
                if distB[i] != -1:
                    ret.append(i)
                a = True
            if edges[j] != -1 and distB[edges[j]] == -1:
                j = edges[j]
                distB[j] = k
                if distA[j] != -1:
                    ret.append(j)
                b = True
            if len(ret):
                return min(ret)
            k += 1
            if not a and not b:
                break
        return -1
