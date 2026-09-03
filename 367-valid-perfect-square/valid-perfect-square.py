class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low, high = 1, num // 2
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1
        return False
        