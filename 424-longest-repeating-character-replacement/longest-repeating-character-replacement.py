class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        maxWindow = 0
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1
            while seen.values() and sum(seen.values()) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            maxWindow = max(maxWindow, right - left + 1)
        return maxWindow
            