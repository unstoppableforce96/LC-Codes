class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        d = {}
        currentSum = 0
        maximumSum = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            d[nums[right]] = d.get(nums[right], 0) + 1
            if right >= k - 1:
                if len(d) == k:
                    maximumSum = max(maximumSum, currentSum)
                d[nums[left]] -= 1
                currentSum -= nums[left]
                if d[nums[left]] == 0:
                    d.pop(nums[left])
                left += 1
        return maximumSum