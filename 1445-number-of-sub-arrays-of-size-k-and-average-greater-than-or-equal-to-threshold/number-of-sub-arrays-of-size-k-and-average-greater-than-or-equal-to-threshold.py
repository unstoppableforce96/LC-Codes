class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currentSum = 0
        left = 0
        ans = 0
        for right in range(len(arr)):
            currentSum += arr[right]
            if right >= k - 1:
                avg = currentSum / k
                if avg >= threshold:
                    ans += 1
                # Subtracting the left most value from sum
                currentSum -= arr[left]
                left += 1
        return ans