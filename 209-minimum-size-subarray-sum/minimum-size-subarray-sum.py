class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Dynamic Sliding Window
        minSize = float('inf')
        left = 0
        c_sum = 0
        for right in range(len(nums)):
            c_sum += nums[right]
            while c_sum >= target:
                c_sum -= nums[left]
                minSize = min(right - left + 1, minSize)
                left += 1
        return 0 if minSize == float('inf') else minSize