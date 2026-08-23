class Solution:
    def isPalindromic(self, s: str) -> bool:
        ans = ""
        for i in s:
            x = bin(ord(i))[2:]
            x = x.rjust(8, '0')
            ans += x
        i = 0
        j = len(ans) - 1
        while i < j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1
        return True