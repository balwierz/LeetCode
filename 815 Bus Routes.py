class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stop2routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop2routes[stop].append(i)
        dist = 1
        currRoutes = stop2routes[source]
        visited = defaultdict(bool)
        while currRoutes:
            nextRoutes = set()
            for route in currRoutes:
                for stop in routes[route]:
                    if not visited[stop]:
                        if stop == target:
                            return dist
                        visited[stop] = True
                        nextRoutes.update(stop2routes[stop])
            dist += 1
            currRoutes = nextRoutes
        return -1
