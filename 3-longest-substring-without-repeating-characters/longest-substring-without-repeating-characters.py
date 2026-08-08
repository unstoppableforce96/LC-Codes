class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        d = set()
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left += 1
            d.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength