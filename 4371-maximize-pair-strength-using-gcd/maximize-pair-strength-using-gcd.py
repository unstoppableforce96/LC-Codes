class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        mx = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                gcd = math.gcd(nums[i], nums[j])
                mx = max(mx, nums[i] * nums[j] // gcd ** 2)
        return mx