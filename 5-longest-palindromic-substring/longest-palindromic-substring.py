def expand_around_center(left, right, n, s):
    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        for i in range(n):
            odd_pal = expand_around_center(i, i, n, s)
            if len(odd_pal) > len(longest):
                longest = odd_pal
            even_pal = expand_around_center(i, i + 1, n, s)
            if len(even_pal) > len(longest):
                longest = even_pal
        return longest