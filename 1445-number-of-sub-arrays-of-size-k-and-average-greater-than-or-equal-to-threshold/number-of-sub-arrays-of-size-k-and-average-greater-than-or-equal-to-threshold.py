class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        first_window = arr[:k]
        currentSum = sum(first_window)
        count = 0
        if currentSum / k >= threshold:
            count += 1
        for i in range(k, len(arr)):
            # add a new element to the sum
            # subtract the old element
            currentSum = currentSum + arr[i] - arr[i - k]
            if currentSum / k >= threshold:
                count += 1
        return count