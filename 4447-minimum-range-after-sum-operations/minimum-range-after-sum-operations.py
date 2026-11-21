class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        lst = [a, b, c]
        lst.sort(reverse=True)
        while lst[0] > lst[1] + lst[2]:
            lst[0] = lst[1] + lst[2]
            lst.sort(reverse=True)
        return lst[0] - lst[-1]