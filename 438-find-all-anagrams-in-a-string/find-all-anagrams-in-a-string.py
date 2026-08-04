class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = {}
        for i in p: a[i] = a.get(i, 0) + 1
        d = {}
        ans = []
        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            if right >= len(p) - 1:
                if a == d:
                    ans.append(right - len(p) + 1)
                left = right - len(p) + 1
                if s[left] in d:
                    d[s[left]] -= 1
                    if d[s[left]] == 0:
                        d.pop(s[left])
        return ans