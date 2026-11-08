class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        i = j = 0
        ans = []
        p1 = ""
        p2 = ""
        while i < len(s1):
            if s1[i] == s2[j]:
                if p1 and p2:
                    ans.append([p1, p2])
                    p1 = ""
                    p2 = ""
                i += 1
                j += 1
                continue
            else:
                p1 += s1[i]
                p2 += s2[j]
            i += 1
            j += 1
        if p1 and p2:
            ans.append([p1, p2])
        return ans