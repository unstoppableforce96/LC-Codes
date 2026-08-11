class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1
        ans = 0
        seen = {0: [-1]}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum in seen:
                ans = max(ans, i - min(seen[current_sum]))
            seen[current_sum] = seen.get(current_sum, []) + [i]
        return ans