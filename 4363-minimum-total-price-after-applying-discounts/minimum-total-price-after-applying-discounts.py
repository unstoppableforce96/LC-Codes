class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        n = len(prices)
        m = len(discounts)
        i = j = 0
        final_price = 0
        while i < n and j < m:
            final_price += prices[i] * (1 - discounts[j] / 100)
            i += 1
            j += 1
        return final_price + sum(prices[i:])
