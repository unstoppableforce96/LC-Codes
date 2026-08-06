class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Process the first window of size k
        d = {}
        currentSum = 0
        maximumSum = 0
        for i in range(k):
            currentSum += nums[i]
            d[nums[i]] = d.get(nums[i], 0) + 1
        if len(d) == k:
            maximumSum = max(currentSum, maximumSum)

        # Process the rest of the array, by adding new element
        # and removing the left most element since every new addition
        # from here causes the window to grow to k + 1 and to keep
        # it at size k, we must kick out the left most element
        for i in range(k, len(nums)):
            # add new element
            currentSum += nums[i]
            d[nums[i]] = d.get(nums[i], 0) + 1

            # kick out the left most, which is at i - k
            out = nums[i - k]
            currentSum -= out
            d[out] -= 1
            if d[out] == 0:
                d.pop(out)

            # Check the maxSum again
            if len(d) == k:
                maximumSum = max(currentSum, maximumSum)
        return maximumSum