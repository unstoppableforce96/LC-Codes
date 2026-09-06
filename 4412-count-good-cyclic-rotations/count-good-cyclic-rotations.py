class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        final = nums + nums
        prefix = [0]
        for i in range(len(final)):
            prefix.append(prefix[i] + final[i])
        half = n // 2
        ans = 0
        for i in range(n):
            first_half = prefix[i + half] - prefix[i]
            second_half = prefix[i + n] - prefix[i + half]
            if first_half > second_half:
                ans += 1
        return ans