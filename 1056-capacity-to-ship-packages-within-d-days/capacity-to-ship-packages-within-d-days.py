def canShip(weights, days_have, capacity):
    # Find the days_needed to ship all the weights under choosen capacity
    days_needed = 1
    cWeightSum = 0
    for w in weights:
        if cWeightSum + w <= capacity:
            cWeightSum += w
        else:
            days_needed += 1
            cWeightSum = w
    # Compare days_needed <= days_have (Capacity is a valid choice)
    return days_needed <= days_have

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            if canShip(weights, days, mid):
                high = mid
            else:
                low = mid + 1
        return low
