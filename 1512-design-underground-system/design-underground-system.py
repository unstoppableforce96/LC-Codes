class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t) # key-id, value-> (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Pop out the customer from custmers map since the ride / trip is over
        startStation, startTime = self.customers.pop(id)
        trip = startStation, stationName # stationName here is end station, it's cout
        if trip in self.stations:
            # increment the time by new sum
            # increment the count of trips by 1
            self.stations[trip][0] += (t - startTime)
            self.stations[trip][1] += 1
        else:
            self.stations[trip] = [t - startTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = startStation, endStation
        return self.stations[trip][0] / self.stations[trip][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)