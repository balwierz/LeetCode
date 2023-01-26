class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [1000001] * n
        cost[src] = 0
        adj = [[] for _ in range(n)]
        for a, b, c in flights:
            adj[a].append((b, c, ))
        state = {src: 0}
        for k in range(k+2):
            newState = dict()
            for a, d in state.items():
                if cost[a] < d:
                    continue
                cost[a] = d
                for b, c in adj[a]:
                    if d + c < cost[b]:
                        if b in newState:
                            newState[b] = min(newState[b], d + c)
                        else:
                            newState[b] = d + c
            print(newState)
            state = newState
        return cost[dst] if cost[dst] < 1000001 else -1

        
