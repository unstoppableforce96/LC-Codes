class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        maxPossible = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            # shrink()
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxPossible = max(maxPossible, right - left + 1)
        return maxPossible