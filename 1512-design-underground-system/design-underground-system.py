class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers.keys():
            ans = self.customers[id][0], stationName
            if ans in self.stations.keys():
                newSum = self.stations[ans][0] + (t - self.customers[id][1] )
                newCount = self.stations[ans][1] + 1
                self.stations[ans] = (newSum, newCount)
            else:
                self.stations[ans] = (t - self.customers[id][1], 1)
            self.customers.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.stations[key][0] / self.stations[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)