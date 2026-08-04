class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_length = 10000000
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                curr_sum -= nums[left]
                min_length = min(min_length, right - left + 1)
                left += 1
        return min_length if not min_length == 10000000 else 0