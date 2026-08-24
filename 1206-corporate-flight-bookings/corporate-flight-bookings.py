class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)
        for i in bookings:
            l, r, val = i
            diff[l] += val
            diff[r + 1] -= val
        # Line Sweep (All ranges are updated, find prefix)
        print(diff)
        prefix = []
        rs = 0
        for i in diff:
            rs += i
            prefix.append(rs)
        
        # Answer array (Addition of original[i] + prefix[i])
        ans = []
        for i in range(1, n + 1):
            ans.append(prefix[i])
        return ans
