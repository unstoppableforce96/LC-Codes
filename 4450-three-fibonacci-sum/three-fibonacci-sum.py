class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b = 0, 1
        while a <= n:
            c = a + b
            if a + b + c == n:
                return True
            a, b = b, c
        return False