class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        currentSum = 0
        maximumSum = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            d[nums[right]] = d.get(nums[right], 0) + 1
            if right >= k - 1:
                if len(d) == k:
                    maximumSum = max(maximumSum, currentSum)
                d[nums[right - k + 1]] -= 1
                currentSum -= nums[right - k + 1]
                if d[nums[right - k + 1]] == 0:
                    d.pop(nums[right - k + 1])
        return maximumSum