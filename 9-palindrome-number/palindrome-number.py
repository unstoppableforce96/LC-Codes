def get_reverse(n: int) -> int:
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x  < 0: return False
        return x == get_reverse(x)
