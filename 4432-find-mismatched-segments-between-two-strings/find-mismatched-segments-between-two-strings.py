class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        s1 += 'A'
        s2 += 'A'
        ans = []
        p1 = p2 = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                p1 += s1[i]
                p2 += s2[i]
            else:
                if p1 and p2:
                    ans.append([p1, p2])
                p1 = ""
                p2 = ""
            i += 1
        return ans