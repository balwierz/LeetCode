class Node:
    def __init__(self, reward):
        self.neigh = []
        self.whenOpen = inf
        self.reward = reward
        self.stepTo0 = None
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        nodes = [Node(v) for v in amount]
        for a, b in edges:
            nodes[a].neigh.append(b)
            nodes[b].neigh.append(a)
        q = [(0, -1)]
        broken = False
        while q:
            q2 = []
            for i, prev in q:
                for n in nodes[i].neigh:
                    if n != prev:
                        nodes[n].stepTo0 = i
                        if n == bob:
                            broken = True
                            break
                        q2.append((n, i))
                if broken:
                    break        
            if broken:
                break
            q = q2
        t = 0
        while bob != 0:
            nodes[bob].whenOpen = t
            bob = nodes[bob].stepTo0
            print(bob)
            t += 1
        ret = -inf
        q = [(0, amount[0], -1)]
        t = 1
        while q:
            print(q)
            q2 = []
            for i, a, prev in q:
                if i and len(nodes[i].neigh) == 1: #only the parent
                    ret = max(ret, a)
                for n in nodes[i].neigh:
                    if n == prev:
                        continue
                    reward = a
                    if t == nodes[n].whenOpen:
                        reward += nodes[n].reward // 2
                    elif t < nodes[n].whenOpen:
                        reward += nodes[n].reward
                    q2.append((n, reward, i))
            t += 1
            q = q2
        return ret
