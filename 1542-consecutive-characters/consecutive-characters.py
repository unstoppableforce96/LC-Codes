class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        maxCount = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]: # same characters
                count += 1
            else:
                maxCount = max(maxCount, count) # update max
                count = 1 # set the count back to 1
        return max(maxCount, count)