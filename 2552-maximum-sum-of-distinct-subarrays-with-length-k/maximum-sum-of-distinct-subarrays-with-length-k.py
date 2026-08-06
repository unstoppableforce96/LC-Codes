class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        currentSum = 0
        maximumSum = 0
        left = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            d[nums[right]] = d.get(nums[right], 0) + 1
            if right - left > k - 1:
                currentSum -= nums[left]
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    d.pop(nums[left])
                left += 1
            if len(d) == k:
                maximumSum = max(currentSum, maximumSum)
        return maximumSum