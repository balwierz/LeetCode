class Solution:
    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        def constantFactory(value):
            return lambda : value
        dp = [defaultdict(constantFactory(0)) for _ in range(n+2)]
        dp[0][0] = startFuel
        stations = [[0, 0]] + stations
        stations.append([target, 0])  # the final station
        for i in range(0, n+1):  # n+1 is the stop, 0 is the start, and 1 stations in between
            #print("i=" + str(i))
            for step, maxFuel in dp[i].items():
                # consider each possible jump
                #print("step " + str(step) + " maxFuel " + str(maxFuel))
                for j in range(i+1, n+2):
                    #print("    j=" + str(j))
                    if stations[j][0] - stations[i][0] <= maxFuel:
                        # there is enough fuel to reach station j from i
                        #if j == n+1:
                            # we reached the last station
                        #    return step  # greedy return
                        dp[j][step+1] = max(dp[j][step+1], maxFuel +
                                            stations[j][1] - stations[j][0] + stations[i][0])
                        #print("dp[" + str(j) + "][" + str(step+1) + "]=" + str(dp[j][step+1]))
                    else:
                        #print("       unreachable")
                        break  # because we cannot visit the stations further away
        if dp[n+1]:
            return min(dp[n+1].keys() ) -1
        return -1
    
    
    def minRefuelStops3(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1
    
    
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, 0))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans
