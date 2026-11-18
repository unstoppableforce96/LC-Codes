class Solution:
    def minChanges(self, s: str) -> int:
        odd_count = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if count % 2 == 1:
                    odd_count += 1
                    count = 0
                else:
                    count = 1
            else:
                count += 1
        if count % 2 == 1:
            odd_count += 1
        return odd_count