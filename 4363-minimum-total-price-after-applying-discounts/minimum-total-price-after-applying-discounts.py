class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        n = len(prices)
        m = len(discounts)
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        k = min(n, m)
        ans = sum(prices[k:])
        i = j = 0
        while i < n and j < m:
            ans += prices[i] * (1 - discounts[j] / 100)
            i += 1
            j += 1
        return ans