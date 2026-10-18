class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ans += 1
        return ans