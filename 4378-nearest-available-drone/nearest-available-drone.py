class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        minRange = float('inf')
        ans = -1
        for i, v in enumerate(drones):
            dist = abs(v[0] - target[0]) + abs(v[1] - target[1])
            if dist <= v[2]:
                if dist < minRange:
                    minRange = dist
                    ans = i
        return ans