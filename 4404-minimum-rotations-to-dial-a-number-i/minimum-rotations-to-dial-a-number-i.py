def get_dist(a, b):
    d1 = abs(a - b)
    x = max(a, b)
    y = min(a, b)
    d2 = 10 - x + y
    return min(d1, d2)
class Solution:
    def minRotations(self, s: str) -> int:
        prev = 0
        ans = 0
        for i in s:
            current = int(i)
            ans += get_dist(prev, current)
            prev = current
        return ans