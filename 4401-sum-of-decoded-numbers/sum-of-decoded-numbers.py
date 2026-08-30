def get_xy(d, width):
    return int(str(d)[:width]), int(str(d)[width:])

def split(n):
    width = n % 10
    d = n // 10
    return get_xy(d, width)
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        ans = 0
        MOD = int(1e9) + 7
        for i in nums:
            x, y = split(i)
            ans = (ans + pow(x, y, MOD)) % MOD
        return ans