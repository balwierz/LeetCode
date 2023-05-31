class UndergroundSystem:

    def __init__(self):
        self.activeTravel = {}  # id to start, time
        self.stats = defaultdict(lambda: defaultdict(lambda : (0, 0)))  # [start][end] -> (sumTimes, nRides)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.activeTravel[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.activeTravel[id]
        del self.activeTravel[id]
        sumTimes, nRides = self.stats[startStation][stationName]
        sumTimes += t-startTime
        nRides += 1
        self.stats[startStation][stationName] = (sumTimes, nRides)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sumTimes, nRides = self.stats[startStation][endStation]
        return sumTimes / nRides
