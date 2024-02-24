class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = [i for i in range(n)]
        members = [[i] for i in range(n)]
        hasSecret = [False] * n
        hasSecret[0] = True
        hasSecret[firstPerson] = True
        allSecret = [0, firstPerson]
        def root(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def gettime(meeting):
            return meeting[2]
        for time, meetingL in groupby(sorted(meetings, key = gettime), key = gettime):
            mentioned = []
            for x, y, t in meetingL:
                if hasSecret[x] and hasSecret[y]:
                    continue  # they both know it already
                elif not hasSecret[x] and not hasSecret[y]:
                    mentioned.append(x)
                    mentioned.append(y)
                    rx, ry = root(x), root(y)
                    if rx != ry:
                        parent[ry] = rx
                        members[rx].extend(members[ry])
                        if hasSecret[ry]:
                            hasSecret[rx] = True
                            hasSecret[ry] = False
                    continue
                elif hasSecret[y]:
                    x, y = y, x
                # now hasSecret[x] == True, hasSecret[y] == False
                mentioned.append(y)
                ry = root(y)
                hasSecret[ry] = True
            for m in mentioned:
                if parent[m] == m:  # is a root of some tree
                    if hasSecret[m]:
                        allSecret.extend(members[m])
            for m in mentioned:
                if parent[m] == m:  # is a root of some tree
                    if hasSecret[m]:
                        for member in members[m]:
                            hasSecret[member] = True
                members[m] = [m]  # reset
                parent[m] = m
        return list(set(allSecret))
