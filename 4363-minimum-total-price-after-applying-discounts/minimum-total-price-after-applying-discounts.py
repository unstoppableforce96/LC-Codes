class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        n = len(prices)
        m = len(discounts)
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        k = min(n, m)
        ans = sum(prices[k:])
        for p in range(k):
            ans += prices[p] * (1 - discounts[p] / 100)
        return ans