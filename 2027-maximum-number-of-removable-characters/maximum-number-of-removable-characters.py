def issubseq(s, t, remove, k):

    s = s.copy()

    for i in range(k):
        s[remove[i]] = '-'

    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1

    return j == len(t)


class Solution:

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        low = 0
        high = len(removable)

        s = list(s)
        t = list(p)

        while low < high:

            mid = (low + high + 1) // 2

            if issubseq(s, t, removable, mid):
                low = mid
            else:
                high = mid - 1

        return low