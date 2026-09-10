def canRepair(ranks, cars_to_be_repaired, time):
    cars_can_be_repaired = 0 
    # Just check if cars_can_be_repaired in time are >= cars_need_to_repaired
    for rank in ranks:
        n = int(math.sqrt(time / rank))
        cars_can_be_repaired += n
    return cars_can_be_repaired >= cars_to_be_repaired

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = min(ranks) * cars * cars
        while low < high:
            mid = (low + high) // 2
            if canRepair(ranks, cars, mid):
                high = mid
            else:
                low = mid + 1
        return low