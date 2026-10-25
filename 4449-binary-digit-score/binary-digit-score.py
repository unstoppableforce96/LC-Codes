class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = s2 = 0
        while a:
            if a & 1:
                s1 += 1
            a >>= 1
        while b:
            if b & 1:
                s2 += 1
            b >>= 1
        return s1 * s2 if s1 >= s2 else s2 // s1