class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        fuel = 0
        def nPeople(node, parent):
            nonlocal fuel
            ret = 0
            for n in neigh[node]:
                if n == parent:
                    continue
                np = nPeople(n, node)
                fuel += math.ceil(np / seats)
                ret += np
            return ret + 1
        numCity = len(roads) + 1
        neigh = [[] for _ in range(numCity)]
        for a, b in roads:
            neigh[a].append(b)
            neigh[b].append(a)
        nPeople(0, -1)
        return fuel
