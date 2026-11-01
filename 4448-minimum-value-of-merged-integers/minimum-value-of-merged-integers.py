class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = int(1e9)
        for i in range(0, len(nums), 2):
            new_num = str(nums[i]) + str(nums[i + 1])
            ans = min(ans, int(new_num))
        return ans