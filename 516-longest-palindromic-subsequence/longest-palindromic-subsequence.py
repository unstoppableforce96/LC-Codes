class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for i in range(len(s))]
        
        # Fill the first diagonal (intervals of 1)
        for i in range(len(s)):
            dp[i][i] = 1

        # Traverse diagonals to build answers for dp[left][right]
        for length in range(2, len(s) + 1):
            for left in range(len(s) - length + 1):
                right = left + length - 1
                if s[left] == s[right]:
                    inside = dp[left + 1][right - 1] if length > 2 else 0
                    dp[left][right] = 2 + inside
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
        return dp[0][len(s) - 1]